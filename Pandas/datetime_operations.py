import pandas as pd

df = pd.DataFrame({
    "Event": ["Admission", "Exam", "Result"],
    "Date": ["2026-01-10", "2026-03-15", "2026-04-20"],
})

# Convert text to pandas datetime values.
df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.month_name()
df["Day_Name"] = df["Date"].dt.day_name()

print("Date information:")
print(df)

print("\nEvents after February 1, 2026:")
print(df[df["Date"] > "2026-02-01"])
