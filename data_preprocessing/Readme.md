# Sentiment Analysis Preprocessing

This folder contains the scripts (`data_cleaning.py` and `data_analysis.py`) for the Sentiment Analysis dataset.

### **05/03/2026**

## Data Cleaning:
- **Dropped Columns**: Removed the redundant `Unnamed: 0` index column.

- **Handled Missing Data**: Filled blank `Retweets` and `Likes` with `0`. Dropped records missing a `Text` or `Sentiment`.

- **Text Formatting**: Stripped trailing spaces from all string columns and lowercased the main `Text` column.

- **Data Types**: Cast numeric fields to integers and parsed the `Timestamp` field into proper datetime objects.

- **Cleanup**: Renamed columns for readability, removed duplicate rows, and sorted the final outputs by highest `Likes` first.

The output is saved back out as `cleaned_sentimentdataset.csv` and is ready for model training and analysis.

### **06/03/2026**

## Data Analysis:
In `data_analysis.py`, several advanced data manipulations were performed:
- **Date Changing:** Extracted `year` and `month` from the `Timestamp` field.

- **Groupby Operations:** Aggregated metrics grouped by `social_platform`.

- **Merging:** Merged additional platform metadata into the dataset.

- **Concatenation:** Demonstrated data concatenation.

- **Correlation:** Calculated the correlation matrix between `Likes` and `Retweets`.
The final engineered data is saved to `data_analysis.csv`.
