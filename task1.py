
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    r"C:\Users\MUSKAN\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_38144 (1).csv",
    skiprows=4
)

exclude = [
    "World",
    "IDA & IBRD total",
    "IBRD only",
    "Middle income",
    "Low & middle income",
    "Lower middle income",
    "Upper middle income",
    "East Asia & Pacific",
    "Early-demographic dividend",
    "Late-demographic dividend"
]

data = data[~data["Country Name"].isin(exclude)]

top10 = data[["Country Name", "2024"]]
top10 = top10.dropna()
top10 = top10.sort_values(by="2024", ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(top10["Country Name"], top10["2024"])

plt.title("Top 10 Countries by Population (2024)")
plt.xlabel("Country")
plt.ylabel("Population")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("population_chart.png")
plt.show()