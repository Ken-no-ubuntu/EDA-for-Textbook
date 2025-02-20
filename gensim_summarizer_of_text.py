import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim.summarization import summarize


# Sample text (you can load from a file)
with open('extracted_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Summarize the text (adjust the ratio to control summary length)
summary = summarize(text, ratio=0.2)  # 20% of the original text

# Print the summary
print(summary)
