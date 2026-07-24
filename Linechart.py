import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("/storage/emulated/0/Internship.vani/Covid19 India (Jan 20 - Mar 20).csv")

# Convert columns
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
df["ConfirmedIndianNational"] = pd.to_numeric(df["ConfirmedIndianNational"], errors="coerce").fillna(0)

# Group by date
line_data = df.groupby("Date")["ConfirmedIndianNational"].sum()

# Plot
plt.figure(figsize=(10,5))
plt.plot(line_data.index, line_data.values, marker='o')

plt.title("Confirmed Indian Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Indian Cases")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()