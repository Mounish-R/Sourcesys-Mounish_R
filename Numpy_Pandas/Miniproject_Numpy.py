import numpy as np

np.random.seed(42)

# 30 days, 5 food items
orders = np.random.randint(10, 100, size=(30, 5))
print("Orders Data:\n", orders)

# 1. Total orders per day
daily_total = np.sum(orders, axis=1)
print("\nTotal Orders Per Day:\n", daily_total)

# 2. Total orders per item
item_total = np.sum(orders, axis=0)
print("\nTotal Orders Per Item:\n", item_total)

# 3. Most popular item
best_item = np.argmax(item_total)
print("\nMost Popular Item Index:", best_item)

# 4. Best sales day
best_day = np.argmax(daily_total)
print("Best Day Index:", best_day)

# 5. Average daily orders
daily_avg = np.mean(daily_total)
print("\nAverage Orders Per Day:", daily_avg)

# 6. Low sales days (below average)
low_days = np.where(daily_total < daily_avg)
print("\nLow Sales Days:\n", low_days)

# 7. Ranking items (from lowest to highest)
ranking = np.argsort(item_total)
print("\nItem Ranking (Low to High):\n", ranking)

# 8. Normalize data (0–1 scale)
min_val = orders.min()
max_val = orders.max()
normalized_orders = (orders - min_val) / (max_val - min_val)
print("\nNormalized Orders:\n", normalized_orders)