# Terminal Chatbot Using Django and ChatterBot

This project implements a terminal-based chatbot using Django and the ChatterBot library, structured using Clean Architecture principles. The chatbot is trained on the English corpus and responds to user queries interactively through the command line.

---

## 📦 Features
- Terminal-based chatbot interaction
- English corpus-based training
- Clean architecture structure
- Easily extensible and maintainable

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/nacharya01/mscs633b02_assignment3
cd mscs633b02_assignment3
```

### 2. (Optional) Create and Activate Virtual Environment
```bash
python -m venv env
source env/bin/activate        
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download spaCy English Model (Important!)
```bash
python -m spacy download en_core_web_sm
```

### 5. Run the Chatbot
```bash
python main.py
```

---

## 📝 Example Conversation
```
user: Good morning! How are you doing?
bot: I am doing very well, thank you for asking.
user: You're welcome.
bot: Do you like hats?
```

---

## 📂 Project Structure
```
.
├── main.py                     # Main chatbot script
├── db.sqlite3                 # SQLite database used by ChatterBot
├── requirements.txt           # Python package dependencies
├── README.md                  # Project documentation
```

---

## 🧾 requirements.txt
```
django==5.2.4
chatterbot==1.2.7
chatterbot_corpus
spacy==3.8.7
pyyaml
```

> 🔔 Don't forget to run:
> ```bash
> python -m spacy download en_core_web_sm
> ```

---

## 🪪 License
MIT License

---
