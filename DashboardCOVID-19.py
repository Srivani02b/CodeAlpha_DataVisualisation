import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("/storage/emulated/0/Internship.vani/Covid19 India (Jan 20 - Mar 20).csv")

# Convert columns
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")

cols = ["ConfirmedIndianNational", "ConfirmedForeignNational", "Cured", "Deaths"]
for col in cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# Create Dashboard
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Dashboard Title
fig.suptitle(
    "COVID-19 Data Visualization Dashboard\n(January 2020 - March 2020)",
    fontsize=16,
    fontweight="bold"
)

# ------------------ Line Chart ------------------
line_data = df.groupby("Date")["ConfirmedIndianNational"].sum()

axs[0,0].plot(line_data.index, line_data.values, marker="o")
axs[0,0].set_title("Trend of Confirmed Indian Cases")
axs[0,0].set_xlabel("Date")
axs[0,0].set_ylabel("Confirmed Cases")
axs[0,0].tick_params(axis='x', rotation=45)

# ------------------ Bar Chart ------------------
state_data = df.groupby("State/UnionTerritory")["ConfirmedIndianNational"].sum()

axs[0,1].bar(state_data.index, state_data.values)
axs[0,1].set_title("Confirmed Cases by State")
axs[0,1].tick_params(axis='x', rotation=90)

# ------------------ Pie Chart ------------------
values = [
    df["ConfirmedIndianNational"].sum(),
    df["ConfirmedForeignNational"].sum(),
    df["Cured"].sum(),
    df["Deaths"].sum()
]

labels = [
    "Indian",
    "Foreign",
    "Cured",
    "Deaths"
]

axs[1,0].pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
axs[1,0].set_title("Cases Distribution")

# ------------------ Scatter Plot ------------------
axs[1,1].scatter(
    df["ConfirmedIndianNational"],
    df["Deaths"]
)

axs[1,1].set_title("Confirmed Cases vs Deaths")
axs[1,1].set_xlabel("Confirmed Cases")
axs[1,1].set_ylabel("Deaths")

# Dashboard Summary
plt.figtext(
    0.5,
    0.01,
    "Summary: This dashboard analyzes COVID-19 data from January to March 2020.\n"
    "The line chart shows an increasing trend in confirmed cases.\n"
    "The bar chart compares confirmed cases across states.\n"
    "The pie chart shows the distribution of confirmed, cured, and death cases.\n"
    "The scatter plot shows the relationship between confirmed cases and deaths.\n"
    "Note: This analysis is based only on the January–March 2020 dataset.",
    ha="center",
    fontsize=9
)

plt.tight_layout(rect=[0, 0.08, 1, 0.93])
plt.show()