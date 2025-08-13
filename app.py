# app.py
import streamlit as st
import pandas as pd
import spacy
import re

# -----------------------------
# Page & Styles
# -----------------------------
st.set_page_config(page_title="Cricket Chatbot • Hundreds", page_icon="🏏", layout="centered")

# Inject CSS (ChatGPT-like bubbles + bottom input)
st.markdown("""
<style>
.stApp { background: #f7f9fb; }
h1 { text-align:center; margin-top: 8px; }
.chat-wrap { max-width: 820px; margin: 0 auto 96px auto; }
.msg { padding: 12px 14px; border-radius: 16px; margin: 8px 0; font-size: 16px; line-height: 1.45; }
.bot  { background: #ececec; color: #111; width: fit-content; max-width: 85%; border-top-left-radius: 6px; }
.user { background: #1677ff; color: white; width: fit-content; max-width: 85%; margin-left: auto; border-top-right-radius: 6px; }
.footer {
  position: fixed; left: 0; right: 0; bottom: 0; z-index: 999;
  background: linear-gradient(180deg, rgba(247,249,251,0.6) 0%, #f7f9fb 45%);
  padding: 14px 16px 18px 16px; backdrop-filter: blur(6px); border-top: 1px solid #e6e9ee;
}
.footer-inner { max-width: 820px; margin: 0 auto; }
.footer .stTextInput > div > div {
  border: 1px solid #d0d7e2; border-radius: 22px; padding: 6px 12px;
  background: white; box-shadow: 0 1px 2px rgba(16,24,40,.04);
}
.footer input { font-size: 16px !important; padding: 12px 6px !important; }
.hint { font-size: 12px; color: #6b7280; margin-top: 6px; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🏏 Cricket Hundreds Chatbot</h1>", unsafe_allow_html=True)
st.caption("Ask about centuries in **Tests, ODIs, T20Is**. Try: *“How many ODI hundreds does Virat have?”*, *“Sachin Test centuries?”*, or just say *hi* 🙂")

# -----------------------------
# Data & NLP
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("cricket_data.csv")  # CSV with Player,Tests,ODIs,T20Is
    df["norm_name"] = df["Player"].str.lower().str.replace(r"\s+", " ", regex=True)
    return df

df = load_data()

@st.cache_resource
def load_nlp():
    return spacy.load("en_core_web_sm")

nlp = load_nlp()

# -----------------------------
# Utils
# -----------------------------
SMALL_TALK = {
    "hello": "👋 Hello! Ask me about cricket hundreds — Tests, ODIs or T20Is.",
    "hi": "👋 Hi! I can tell you how many centuries a player has in each format.",
    "hey": "👋 Hey there! Try: *How many ODI hundreds does Kohli have?*",
    "thanks": "😊 You’re welcome! Ask me another cricket question.",
    "thank you": "😊 Happy to help!",
    "bye": "👋 Goodbye! Come back anytime for more cricket stats.",
    "goodbye": "👋 See you! Keep smashing questions like centuries."
}

FORMAT_MAP = {
    "tests": ["test", "tests"],
    "odis": ["odi", "odis", "one day", "one-day"],
    "t20is": ["t20", "t20i", "t20is"],
    "total": ["total", "overall", "all formats", "allformat", "all-format"]
}

def detect_small_talk(text: str):
    t = text.lower().strip()
    for k, v in SMALL_TALK.items():
        if re.search(rf"\b{k}\b", t):
            return v
    return None

def find_player(text: str):
    t = " " + re.sub(r"\s+", " ", text.lower()).strip() + " "
    for _, row in df.iterrows():
        cand = " " + row["norm_name"] + " "
        if cand in t:
            return row["Player"]
    doc = nlp(text)
    tokens = [tok.text.lower() for tok in doc if tok.is_alpha and len(tok.text) > 2]
    best = None
    best_hits = 0
    for _, row in df.iterrows():
        name_tokens = row["norm_name"].split()
        hits = sum(1 for nt in name_tokens if nt in tokens)
        if hits > best_hits and hits >= 2:
            best, best_hits = row["Player"], hits
    return best

def detect_format(text: str):
    t = text.lower()
    for fmt_key, keys in FORMAT_MAP.items():
        for k in keys:
            if k in t:
                return fmt_key
    return None

def format_answer(player: str, fmt_key: str):
    row = df.loc[df["Player"] == player].iloc[0]
    if fmt_key == "tests":
        return f"🏆 **{player}** has scored **{row['Tests']}** hundreds in **Tests**."
    if fmt_key == "odis":
        return f"🏆 **{player}** has scored **{row['ODIs']}** hundreds in **ODIs**."
    if fmt_key == "t20is":
        return f"🏆 **{player}** has scored **{row['T20Is']}** hundreds in **T20Is**."
    total = int(row["Tests"]) + int(row["ODIs"]) + int(row["T20Is"])
    return f"🏅 **{player}** has scored **{total}** hundreds **across all formats** (Tests: {row['Tests']}, ODIs: {row['ODIs']}, T20Is: {row['T20Is']})."

def default_player_card(player: str):
    row = df.loc[df["Player"] == player].iloc[0]
    return f"📊 **{player}** — Tests **{row['Tests']}**, ODIs **{row['ODIs']}**, T20Is **{row['T20Is']}**."

# -----------------------------
# Session State Initialization
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hi! I’m your cricket hundreds assistant. Ask me about any player’s centuries in Tests, ODIs or T20Is."}
    ]

if "last_user_message" not in st.session_state:
    st.session_state.last_user_message = ""

# -----------------------------
# Chat Display
# -----------------------------
st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)
for m in st.session_state.messages:
    if m["role"] == "user":
        st.markdown(f'<div class="msg user">{m["text"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="msg bot">{m["text"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Turn Handling
# -----------------------------
def handle_user(text: str):
    text = text.strip()
    if not text:
        return
    st.session_state.messages.append({"role": "user", "text": text})

    st_reply = detect_small_talk(text)
    if st_reply:
        st.session_state.messages.append({"role": "bot", "text": st_reply})
        return

    player = find_player(text)
    fmt_key = detect_format(text)

    if player and fmt_key:
        reply = format_answer(player, fmt_key)
    elif player and not fmt_key:
        reply = default_player_card(player)
    else:
        reply = ("❌ I couldn’t find the player in my database or understand the format.\n\n"
                 "• Try including a player name (e.g., **Virat Kohli**, **Sachin Tendulkar**)\n"
                 "• Mention a format: **Tests**, **ODIs**, **T20Is**, or **total**")

    st.session_state.messages.append({"role": "bot", "text": reply})

# Check & handle new message BEFORE widget is created
if "pending_input" in st.session_state and st.session_state.pending_input:
    handle_user(st.session_state.pending_input)
    st.session_state.last_user_message = st.session_state.pending_input
    st.session_state.pending_input = ""  # reset before rendering widget
    st.rerun()

# -----------------------------
# Bottom Input (sticky footer)
# -----------------------------
with st.container():
    st.markdown('<div class="footer"><div class="footer-inner">', unsafe_allow_html=True)
    user_text = st.text_input(
        "Type your message",
        key="pending_input",
        placeholder="Type your message… (e.g., How many ODI hundreds does Virat Kohli have?)",
        label_visibility="collapsed",
    )
    st.markdown('<div class="hint">Press Enter to send • I currently know *hundreds* only</div>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)
