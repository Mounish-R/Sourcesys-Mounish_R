import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Mydataset.csv")

df = df.drop(columns=["transaction_id", "user_id"], errors="ignore")
df = df.dropna()

for col in df.select_dtypes(include="object").columns:
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop("addicted_label", axis=1)
y = df["addicted_label"]

model = KNeighborsClassifier(n_neighbors=3)

scores = cross_val_score(model, X, y, cv=5)

print("Cross Validation Scores:", scores)
print("Average Accuracy:", scores.mean())