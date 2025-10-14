#Amelia Wilson
"""
CP1404 Practical 5
Estimate: 30 mins
Actual:  mins
"""

text = input("Text: ")
words = text.split()
word_to_count = {}

for word in words:

    word = word.lower()
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

sorted_words = sorted(word_to_count.keys())
max_length = max(len(word) for word in sorted_words)