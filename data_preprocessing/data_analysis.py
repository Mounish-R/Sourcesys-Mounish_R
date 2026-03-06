import pandas as pd
import numpy as np

df = pd.read_csv("cleaned_sentimentdataset.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["year"] = df["Timestamp"].dt.year
df["month"] = df["Timestamp"].dt.month

avg_likes = df.groupby("social_platform")["Likes"].mean()
count_posts = df.groupby("social_platform")["review_text"].count()
sum_retweets = df.groupby("social_platform")["Retweets"].sum()
multiple_aggregations = df.groupby("social_platform")["Likes"].agg(["mean", "sum", "count"])

platform_info = {
    "social_platform": ["Twitter", "Instagram", "Facebook"],
    "platform_type": ["Microblogging", "Photo Sharing", "Social Networking"]
}
platform_df = pd.DataFrame(platform_info)

merged_df = pd.merge(df, platform_df, on="social_platform", how="left")

concat_df = pd.concat([merged_df, merged_df.head(50)])

correlation_analysis = merged_df[["Likes", "Retweets"]].corr()

merged_df.to_csv("data_analysis.csv", index=False)
