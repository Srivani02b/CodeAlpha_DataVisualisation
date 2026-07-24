import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("/storage/emulated/0/Internship.vani/Covid19 India (Jan 20 - Mar 20).csv")

# Convert ConfirmedIndianNational to numeric
df["ConfirmedIndianNational"] = pd.to_numeric(
    df["ConfirmedIndianNational"], errors="coerce"
).fillna(0)

# Group by State
state_data = df.groupby("State/UnionTerritory")["ConfirmedIndianNational"].sum()

# Create Bar Chart
plt.figure(figsize=(12,6))
state_data.plot(kind="bar")

plt.title("Confirmed Indian Cases by State")
plt.xlabel("State/Union Territory")
plt.ylabel("Confirmed Indian Cases")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()