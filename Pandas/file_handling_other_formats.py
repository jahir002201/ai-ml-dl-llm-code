import pandas as pd
from pathlib import Path

df = pd.DataFrame({
    "City": ["Dhaka", "Mymensingh", "Chattogram"],
    "Population_Millions": [10.2, 0.6, 5.2],
})

# JSON support is built into pandas.
df.to_json("cities.json", orient="records", indent=4)
print("JSON data:")
print(pd.read_json("cities.json"))

# HTML export creates a table that can be opened in a browser.
df.to_html("cities.html", index=False)
print("\nCreated:", Path("cities.json").resolve())
print("Created:", Path("cities.html").resolve())

# Optional formats:
# Parquet: pip install pyarrow
# df.to_parquet("cities.parquet", index=False)
# print(pd.read_parquet("cities.parquet"))
