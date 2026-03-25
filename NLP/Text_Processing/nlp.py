import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = "I am learning Natural Language Processing to build smart AI applications."

# Tokenization
tokens = word_tokenize(text)

# Load stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords + punctuation
filtered_tokens = [word for word in tokens if word.isalnum() and word.lower() not in stop_words]

# Output
print("\nNLP Processing Output")
print("Original Text:", text)
print("Tokens:", tokens)
print("Filtered Tokens:", filtered_tokens)