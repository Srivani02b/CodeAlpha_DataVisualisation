import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("/storage/emulated/0/Internship.vani/Covid19 India (Jan 20 - Mar 20).csv")

# Convert columns to numeric
df["ConfirmedIndianNational"] = pd.to_numeric(df["ConfirmedIndianNational"], errors="coerce").fillna(0)
df["Deaths"] = pd.to_numeric(df["Deaths"], errors="coerce").fillna(0)

# Create Scatter Plot
plt.figure(figsize=(8,6))

plt.scatter(
    df["ConfirmedIndianNational"],
    df["Deaths"],
    alpha=0.7
)

plt.title("Relationship Between Confirmed Cases and Deaths")
plt.xlabel("Confirmed Indian Cases")
plt.ylabel("Deaths")
plt.grid(True)

plt.show()