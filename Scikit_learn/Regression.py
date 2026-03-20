import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

df = pd.read_csv("Mydataset.csv")

df = df.drop(columns=["transaction_id", "user_id"], errors="ignore")
df = df.dropna()
df = pd.get_dummies(df, drop_first=True)

X = df.drop("addicted_label", axis=1)
y = df["addicted_label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lin = LinearRegression()
lin.fit(X_train, y_train)
pred_lin = lin.predict(X_test)

print("Linear Regression")
print("MSE:", mean_squared_error(y_test, pred_lin))
print("R2:", r2_score(y_test, pred_lin))

if y.nunique() == 2:
    log = LogisticRegression(max_iter=1000)
    log.fit(X_train, y_train)
    pred_log = log.predict(X_test)

    print("\nLogistic Regression")
    print("MSE:", mean_squared_error(y_test, pred_log))
    print("R2:", r2_score(y_test, pred_log))
    print("Accuracy:", accuracy_score(y_test, pred_log))