### 🏏 Cricket Hundreds Chatbot

A simple **Streamlit-based NLP chatbot** that answers queries about cricket players’ centuries (hundreds) in **Tests, ODIs, and T20Is**.  
The chatbot uses **spaCy** for Natural Language Processing and a CSV dataset of players with their hundreds.

---

## 📌 Features

- 💬 **ChatGPT-like UI** — user messages on the right, bot replies on the left.
- 🏆 **Cricket hundreds data** — supports Tests, ODIs, T20Is, and total hundreds.
- 🗣 **Small talk support** — responds to greetings like *Hi*, *Hello*, *Thanks*, etc.
- 🔍 **Player name recognition** — finds players even if the name is typed partially.
- 📊 **Full player summary** if no format is specified.
- 📱 **Sticky input bar** at the bottom for a smooth chat experience.

---

## 🗂 Dataset

The app expects a CSV file named `cricket_data.csv` in the project root with the following columns:

| Player             | Tests | ODIs | T20Is |
|--------------------|-------|------|-------|
| Virat Kohli        | 29    | 50   | 1     |
| Sachin Tendulkar   | 51    | 49   | 0     |
| Rohit Sharma       | 10    | 31   | 5     |
| ...                | ...   | ...  | ...   |

> Ensure the column names **exactly match** the above.

---

## 🛠 Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/your-username/cricket-hundreds-chatbot.git
cd cricket-hundreds-chatbot
````

2️⃣ **Create & activate a virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Download spaCy model**

```bash
python -m spacy download en_core_web_sm
```

---

## ▶ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

This will open the chatbot in your browser at:

```
http://localhost:8501
```

---

## 💡 Example Questions

* `How many ODI hundreds does Virat Kohli have?`
* `Sachin Tendulkar Test centuries`
* `Total hundreds of Rohit Sharma`



## 📦 Technologies Used

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/) — UI framework
* [spaCy](https://spacy.io/) — Natural Language Processing
* [pandas](https://pandas.pydata.org/) — Data handling
* [Regex](https://docs.python.org/3/library/re.html) — Text matching

"# -AI-CHATBOT-WITH-NLP" 
