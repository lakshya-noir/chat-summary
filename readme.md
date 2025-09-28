# AI Chat Summarizer 📝🤖

A **command-line tool** to summarize WhatsApp or Discord chats using **AI**, with optional sentiment analysis and participant statistics. Quickly get insights from long conversations without reading everything!

---

## ⭐️ Features

- Supports **WhatsApp (.txt)** and **Discord (.json)** chat exports  
- Generates **AI-powered summaries** of your chats  
- Optional **sentiment analysis** of the summary (Positive / Negative / Neutral)  
- Optional **top participant statistics** to see who’s most active  
- Save summaries to **CSV files** for future reference

---

## 🚀 Installation

1. **Clone the repository**

```bash
git clone git@github.com:lakshya-noir/chat-summary.git
cd chat-summary
```

2. **Set up a virtual environment and install dependencies**

```
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

3. **NLTK resources will be downloaded automatically if missing:**
- Stopwords
- Tokenizer (punkt)

---

## 👾 **Usage**
```
python app.py --input path/to/chatfile
```

**Optional flags :**
```
python app.py --input chats/whatsapp.txt --sentiment --participants

```
- Using ```--sentiments``` provides the user with sentiment analysis of the chat.
- Using ```--particpants``` shows the top 5 most active participants in the chat.

---
