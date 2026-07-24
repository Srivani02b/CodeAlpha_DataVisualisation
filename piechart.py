import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("/storage/emulated/0/Internship.vani/Covid19 India (Jan 20 - Mar 20).csv")

# Convert columns to numeric
df["ConfirmedIndianNational"] = pd.to_numeric(df["ConfirmedIndianNational"], errors="coerce").fillna(0)
df["ConfirmedForeignNational"] = pd.to_numeric(df["ConfirmedForeignNational"], errors="coerce").fillna(0)
df["Cured"] = pd.to_numeric(df["Cured"], errors="coerce").fillna(0)
df["Deaths"] = pd.to_numeric(df["Deaths"], errors="coerce").fillna(0)

# Total values
values = [
    df["ConfirmedIndianNational"].sum(),
    df["ConfirmedForeignNational"].sum(),
    df["Cured"].sum(),
    df["Deaths"].sum()
]

labels = [
    "Indian Confirmed",
    "Foreign Confirmed",
    "Cured",
    "Deaths"
]

# Pie Chart
plt.figure(figsize=(7,7))
plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("COVID-19 Cases Distribution")

plt.show()