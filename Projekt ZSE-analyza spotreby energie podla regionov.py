import pandas as pd
import random
from datetime import datetime, timedelta

regions = ["Bratislava", "Košice", "Prešov", "Nitra", "Trnava"]
start_date = datetime(2025, 12, 1)
days = 30

data = []

for i in range(days):
    date = start_date + timedelta(days=i)
    for region in regions:
        consumption = random.randint(50, 300)
        data.append([region, date.strftime("%Y-%m-%d"), consumption])

df = pd.DataFrame(data, columns=["region", "date", "consumption"])
df["high_usage"] = df["consumption"] > 200
df.to_csv("energy_data.csv", index=False)
print(df)

for i, row in df.iterrows():
    print(f"INSERT INTO energy_data (region, date, consumption, high_usage) VALUES ('{row.region}','{row.date}',{row.consumption},{int(row.high_usage)});")