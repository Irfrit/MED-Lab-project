from pathlib import Path

import pandas as pd

workbook = Path("data/raw/MED-Lab-1-Zadanie-1-Dane.xlsx")
users = pd.read_excel(
    workbook,
    sheet_name=3,
    header=1,
)

users = users.dropna(subset=["Users"]).copy()
users = users[["QY", "Users"]].copy()
users.columns = ["quarter", "users_millions"]

print(users.head())
print(users.tail())
print("Rows:", len(users))
print("Missing values:", users.isna().sum())
