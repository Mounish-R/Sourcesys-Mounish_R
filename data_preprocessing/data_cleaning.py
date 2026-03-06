import pandas as pd
import numpy as np

df = pd.read_csv("sentimentdataset.csv")

if 'Unnamed: 0' in df.columns:
    df.drop(columns=['Unnamed: 0'], inplace=True)

df['Retweets'] = df['Retweets'].fillna(0)
df['Likes'] = df['Likes'].fillna(0)

df = df.dropna(subset=['Text', 'Sentiment'])

df['Text'] = df['Text'].str.strip()
df['Sentiment'] = df['Sentiment'].str.strip()
df['User'] = df['User'].str.strip()
df['Platform'] = df['Platform'].str.strip()
df['Hashtags'] = df['Hashtags'].str.strip()
df['Country'] = df['Country'].str.strip()

df['Text'] = df['Text'].str.lower()

df['Retweets'] = df['Retweets'].astype(int)
df['Likes'] = df['Likes'].astype(int)

df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

df.rename(columns={"Text": "review_text", "Platform": "social_platform"}, inplace=True)

df.drop_duplicates(inplace=True)

sorted_df = df.sort_values(by=["Likes"], ascending=[False])

output_file = "cleaned_sentimentdataset.csv"
sorted_df.to_csv(output_file, index=False)
print(f"Data cleaning complete. File saved to {output_file}.")
