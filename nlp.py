from backend import get_bible_text
import re
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download("stopwords")
def get_wordcloud_data_and_plot(version, book, chapter):

    # Call get_bible_text function
    text = get_bible_text(version=version, book=book, chapter=chapter)

    # Words in text
    pattern = re.compile(r'\b\w+\b')
    findings = re.findall(pattern, text.lower())

    # Capitalize "God" names
    words = []
    holy_words = ["dios", "jehovah", "jesús", "jehová", "altísimo"]
    for word in findings:
        if word in holy_words:
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
    wc = WordCloud(width=1000, height=800, max_words=200, background_color="#00172B",
                   contour_color="black", contour_width=1,
                   include_numbers=True).generate_from_frequencies(sorted_d)
    plt.figure(figsize=(8, 8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=2)
    graph = "wordcloud_fig.png"
    plt.savefig(graph, bbox_inches="tight")

    return sorted_d, graph


if __name__ == "__main__":
    print(get_wordcloud_data_and_plot(version="rva", book="Genesis", chapter=6))
