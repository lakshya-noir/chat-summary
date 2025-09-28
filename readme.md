# AI Chat Summarizer 📝🤖

A powerful **command-line tool** to summarize your WhatsApp or Discord chats using **AI**, with optional sentiment analysis and participant statistics. Quickly get insights from long conversations without reading everything!  

---

## Features

- Supports **WhatsApp (.txt)** and **Discord (.json)** chat exports.  
- Generates **AI-powered summaries** of your chats.  
- Optional **sentiment analysis** of the summary (Positive / Negative / Neutral).  
- Optional **top participant statistics** to see who’s most active.  
- Save summaries to **CSV files** for future reference.  
- Beautiful **color-coded CLI output** for easy reading.  

---

## Installation

1. Clone the repo:

```bash
git clone git@github.com:lakshya-noir/chat-summary.git
cd chat-summary
Create a virtual environment and install dependencies:

bash
Copy code
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
Make sure you have Python 3.8+ installed.

NLTK resources (downloaded automatically if missing):

Stopwords

Tokenizer (punkt)

Usage
Run the script with the required chat file:

bash
Copy code
python app.py --input path/to/chatfile
Optional flags:

Flag	Description
--sentiment	Include sentiment analysis of the summary
--participants	Display top 5 chat participants

Example:

bash
Copy code
python app.py --input chats/whatsapp.txt --sentiment --participants
You’ll be prompted to save the summary to a CSV file if you want.

Output Example
markdown
Copy code
===== Top Participants =====
Alice : 120 messages
Bob   : 95 messages
Charlie : 40 messages
===========================

===== Chat Summary =====
Alice and Bob discussed the project milestones...
========================

===== Sentiment Analysis (of Summary) =====
Sentiment : POSITIVE 😎 (Confidence: 0.95)
=========================================
Dependencies
transformers (HuggingFace pipeline for summarization and sentiment analysis)

nltk (for text processing)

pandas (for saving CSV)

colorama (for CLI colors)

Install all dependencies via:

bash
Copy code
pip install transformers nltk pandas colorama
Notes
First run may download AI models (~1 GB) – subsequent runs are faster.

Works best for text-heavy chats. Large files may take longer to summarize.

License
MIT License © 2025 Lakshya JS

yaml
Copy code

---

If you want, I can also make a **super-short “flashy” GitHub-style version** that grabs attention immediately when someone visits your repo.  

Do you want me to make that too?
