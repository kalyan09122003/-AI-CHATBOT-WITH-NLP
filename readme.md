## CRICKET HUNDREDS CHATBOT

COMPANY: CODTECH IT SOLUTIONS

NAME: Guraka kalyan

INTERN ID : CT06DZ415

DOMAIN: PYTHON

DURATION: 6 WEEKS

MENTOR: NEELA SANTHOSH

##  Project Overview
A simple **Streamlit-based NLP chatbot** that answers queries about cricket players’ centuries (hundreds) in **Tests, ODIs, and T20Is**.  
The chatbot uses **spaCy** for Natural Language Processing and a CSV dataset of players with their hundreds.

---

## Features

- 💬 **ChatGPT-like UI** — user messages on the right, bot replies on the left.
- 🏆 **Cricket hundreds data** — supports Tests, ODIs, T20Is, and total hundreds.
- 🗣 **Small talk support** — responds to greetings like *Hi*, *Hello*, *Thanks*, etc.
- 🔍 **Player name recognition** — finds players even if the name is typed partially.
- 📊 **Full player summary** if no format is specified.
- 📱 **Sticky input bar** at the bottom for a smooth chat experience.




## 🛠 Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/kalyan09122003/-AI-CHATBOT-WITH-NLP.git  
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

## Output
<img width="960" height="483" alt="Screenshot 2025-08-13 115013" src="https://github.com/user-attachments/assets/272a6ae6-3dc9-4afe-857b-2a88b5696986" />



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


