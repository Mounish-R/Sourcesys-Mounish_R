# Email Spam Classifier

## Overview

This project classifies emails as spam or not spam using a machine learning model.

## How It Works

1. The dataset is loaded from a CSV file.
2. The email text is selected as input.
3. The data is split into training and testing sets.
4. Text data is converted into numerical form using TF-IDF.
5. A Naive Bayes model is trained on the training data.
6. The model predicts whether an email is spam or not.

## How to Run

1. Place the dataset file (emails.csv) in the project folder.
2. Run the Python file:

```
python Classifier.py
```

## Output

* Displays email and its prediction (Spam or Not Spam).
* Saves results in a file named `email_output.csv`.

