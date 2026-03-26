from transformers import pipeline

# Example: sentiment analysis
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_input(text):
    result = sentiment_pipeline(text)[0]
    return result