# Made By Divit Kundan
from gensim.summarization import summarize

text = open("document.txt", "r").read()

summary = summarize(text, ratio=0.2)

print("\n--- Summary ---\n")
print(summary)
