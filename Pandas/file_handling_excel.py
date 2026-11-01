import pandas as pd

df = pd.DataFrame({
    "Product": ["Notebook", "Pen", "Bag"],
    "Price": [80, 15, 950],
    "Quantity": [10, 50, 5],
})

# Requires: pip install openpyxl
df.to_excel("products.xlsx", index=False, sheet_name="Products")
loaded_df = pd.read_excel("products.xlsx", sheet_name="Products")

print("Excel data loaded successfully:")
print(loaded_df)
