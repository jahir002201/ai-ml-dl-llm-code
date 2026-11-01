import pandas as pd

df = pd.DataFrame({
    "Product": ["Pen", "Notebook", "Bag"],
    "Price": [15, 80, 950],
    "Quantity": [10, 5, 2],
})

# Arithmetic operations create new columns.
df["Subtotal"] = df["Price"] * df["Quantity"]
df["Discount"] = df["Subtotal"] * 0.10
df["Total"] = df["Subtotal"] - df["Discount"]

# Logical comparisons create Boolean values.
df["Bulk_Order"] = df["Quantity"] >= 5
df["Expensive"] = df["Price"] > 100

print(df)

print("\nTotal sales:", df["Total"].sum())
print("Average product price:", df["Price"].mean())
print("Highest price:", df["Price"].max())
