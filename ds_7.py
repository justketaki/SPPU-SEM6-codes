# Install and import necessary libraries
!pip install nltk
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
import string

# Download necessary NLTK data
nltk.download('punkt', download_dir='./nltk_data')
nltk.download('stopwords', download_dir='./nltk_data')
nltk.download('averaged_perceptron_tagger', download_dir='./nltk_data')

# Input Text
text = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
text = text.lower()
print("Original Text:", text)

# Removing Punctuation
text_p = "".join([char for char in text if char not in string.punctuation])
print("Text without Punctuation:", text_p)

# Tokenization
words = word_tokenize(text_p)
words1 = sent_tokenize(text_p)
print("Words:", words)
print("Sentences:", words1)

# Stopword Filtering
stop_words = stopwords.words('english')
filtered_words = [word for word in words if word not in stop_words]
print("Filtered Words:", filtered_words)

# Stemming
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in filtered_words]
print("Stemmed Words:", stemmed)

# Part-of-Speech Tagging
pos = pos_tag(filtered_words)
print("POS Tagged Words:", pos)

# TF-IDF Calculation
corpus = [text]
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# Get feature names (terms)
terms = tfidf_vectorizer.get_feature_names_out()
print("TF-IDF Terms:", terms)

# Display TF-IDF values for the document
tfidf_values = tfidf_matrix.toarray()
print("TF-IDF Values:", tfidf_values)
