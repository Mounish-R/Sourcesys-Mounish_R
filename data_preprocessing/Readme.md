# Sentiment Analysis Preprocessing

This folder contains the data preprocessing code (`data_cleaning.py`) for the Sentiment Analysis dataset. 

Here is a summary of the cleaning steps performed on the raw data:

- **Dropped Columns**: Removed the redundant `Unnamed: 0` index column.

- **Handled Missing Data**: Filled blank `Retweets` and `Likes` with `0`. Dropped records missing a `Text` or `Sentiment`.

- **Text Formatting**: Stripped trailing spaces from all string columns and lowercased the main `Text` column.

- **Data Types**: Cast numeric fields to integers and parsed the `Timestamp` field into proper datetime objects.

- **Cleanup**: Renamed columns for readability, removed duplicate rows, and sorted the final outputs by highest `Likes` first.

The output is saved back out as `cleaned_sentimentdataset.csv` and is ready for model training and analysis.
