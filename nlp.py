from backend import get_bible_text
import re
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt



text = get_bible_text(version="rva", book="Genesis", chapter=1)

# Words in text
pattern = re.compile(r'\b\w+\b')
findings = re.findall(pattern, text.lower())

# Capitalize "God"
words = []
for word in findings:
    if word == 'dios':
        cap_word = word.capitalize()
        words.append(cap_word)
    else:
        words.append(word)

# Get spanish stopwords
spanish_stopwords = stopwords.words("spanish")

# Filtered words
filtered_words = []
for word in words:
    if word not in spanish_stopwords:
        filtered_words.append(word)

# Dict with total words
d = {}
for word in filtered_words:
    d[word] = d.get(word, 0) + 1

sorted_d = {key: value for key, value in sorted(
    d.items(), reverse=True, key=lambda x: x[1])}

# Get WordCloud Plot
wc = WordCloud(width=800, height=400, max_words=200).generate_from_frequencies(sorted_d)
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()