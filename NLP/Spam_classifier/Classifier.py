import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("emails.csv")

# Try common column formats
if 'text' in df.columns:
    X = df['text']
elif 'message' in df.columns:
    X = df['message']
elif 'subject' in df.columns:
    X = df['subject']
else:
    raise Exception("Text column not found")

if 'spam' in df.columns:
    y = df['spam']
elif 'label' in df.columns:
    y = df['label']
else:
    raise Exception("Label column not found")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)

# Create table output
results = pd.DataFrame({
    'Email': X_test.values,
    'Prediction': y_pred
})

# Convert labels
results['Prediction'] = results['Prediction'].map({0: 'Not Spam', 1: 'Spam'})

print("\n--- Email Classification Table ---")
print(results.head(10))

# Save table
results.to_csv("email_output.csv", index=False)

print("\nSaved as email_output.csv")