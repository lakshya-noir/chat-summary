import argparse # for parsing CLI argument
import os # file existence and file paths
import csv # to save output
import json # for discord json file parsing
import re # regex to split whatsapp messages into fields like time, date, sender, message etc.
from transformers import pipeline # summary using huggingface
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from colorama import Fore, Style # to make the cli output look more appealing
import pandas as pd


try:
    stopwords.words('english')    
except LookupError:
    print("Downloading NLTK stopwords... (only happens once)")
    nltk.download("stopwords") # to install the stopwords

try:
    word_tokenize("test")
except LookupError:
    print("Downloading NLTK tokenizer... (only happens once)")
    nltk.download("punkt") # to install the tokenizer



parser = argparse.ArgumentParser(description="AI Chat Summarizer")

parser.add_argument("--input", required=True, help="Path to the chat file (.txt for WA, .json for Discord)")
parser.add_argument("--sentiment", action="store_true", help="Include sentiment analysis in the output")
parser.add_argument("--participants", action="store_true", help="Include top participants in the output")

args = parser.parse_args()

input_file = args.input
chat_sentiment = args.sentiment
chat_participants = args.participants

def parse_whatsapp(file_path):
	messages = []
	with open(file_path, "r", encoding="utf-8") as f:
		for line in f:
			match = re.match(r"(\d+/\d+/\d+), (\d+:\d+ [APM]+) - (.*?): (.*)", line)
			if match:
				data, time, sender, msg = match.groups()
				messages.append({
					"timestamp":f"{data}{time}",
					"sender":sender,
					"content":msg
				})
	return messages

def parse_discord(file_path):
	messages = []
	with open(file_path, "r", encoding="utf-8") as f:
		data = json.load(f)
		for msg in data:
			messages.append({
			"timestamp":msg["timestamp"],
			"sender":msg["author"],
			"content":msg["content"]
			})
	return messages

if input_file.endswith(".txt"):
	chat_summary = parse_whatsapp(input_file)
elif input_file.endswith(".json"):
	chat_summary = parse_discord(input_file)
else:
	raise ValueError("Unsupported file type. Use .txt for Whatsapp or .json for Discord.")


if chat_participants:
	print("\n===== Top Participants =====\n")
	senders = [msg['sender'] for msg in chat_summary]
	count = Counter(senders)
	for participant, count in count.most_common(5):
		print(f"{participant} : {count} messages")
	print("\n==========================\n")

raw_text = " ".join([msg.get("content", "") for msg in chat_summary])
print("Model downloading... (it's a one time download, relax)")
summarizer = pipeline("summarization")
summary_result = summarizer(raw_text,max_length = 150,min_length = 40, do_sample=False)
# do_sample = False ensures the same summary for the same input file every single time
summary_text = summary_result[0]['summary_text']

print("\n===== Chat Summary =====\n")
print(summary_text)
print("\n========================\n")

if chat_sentiment:
	print("\n===== Sentiment Analysis (of Summary) =====\n")	
	sentiment_analyser = pipeline("sentiment-analysis")
	result = sentiment_analyser(summary_text)[0]
	label = result['label']
	score = result['score']
	if label == "POSITIVE":
		label_colored = Fore.GREEN + "POSITIVE 😎" + Style.RESET_ALL
	elif label == "NEGATIVE":
		label_colored = Fore.RED + "NEGATIVE 😩" + Style.RESET_ALL
	else:
		label_colored = Fore.YELLOW + "Neutral 😴" + Style.RESET_ALL

	print(f"Sentiment : {label_colored} (Confidence : {score:.2f})")
	print("\n=========================================\n")


save_csv = input("Do you want to save this summary to a CSV file? (y/n): ").lower()
if save_csv == "y":
    df = pd.DataFrame({'Summary': [summary_text]})
    filename = "chat_summary.csv"
    df.to_csv(
        filename,
        mode='a',               # 'a' stands for append
        header=not os.path.isfile(filename), # Write header only if file doesn't exist
        index=False,            # Don't write the DataFrame index
        encoding='utf-8'
    )
    print(f"Summary saved to {filename} ✅")