# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: Python (MED Lab)
#     language: python
#     name: med-lab
# ---

# %% [markdown]
# # Co chcemy zbadać i dlaczego?
#
#
# Pytanie 1. Czy liczba użytkowników Mety/Facebooka rośnie liniowo czy lepiej opisuje ją funckja kwadratowa.
#
# Pytanie 2. Czy istnieje zależność między przychodami Mety a liczbą zatrudnionych praconwików? Jeśli tak to jaka jest to zależność
#
# Pytanie 3
#
# Czy modele zbudowane na danych 2007-2017 zachowują zdolność predykcyjną w kolejnych latach?
#

# %%
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import statsmodels.formula.api as smf

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

PROJECT_ROOT = Path.cwd() if (Path.cwd() / "data").exists() else Path.cwd().parent
DATA_DIR = PROJECT_ROOT / "data" / "raw"

WORKBOOK = DATA_DIR / "MED-Lab-1-Zadanie-1-Dane.xlsx"

assert WORKBOOK.exists(), f"File not found: {WORKBOOK}"

print("Workbook:", WORKBOOK)

# %%
annual = pd.read_excel(
    WORKBOOK,
    sheet_name="Użytk-Przych-Zysk-Zatr",
)

annual = annual.rename(columns={
    "Rok": "year",
    "Przychod": "revenue",
    "Zysk": "profit",
    "Zatrudnienie": "employees",
    "Uzytk": "users",
})

annual = annual.dropna(subset=["year"]).copy()

print("Shape:", annual.shape)
print("Missing values:")
display(annual.isna().sum())

display(annual)

# %%
# Convert columns to numeric values.
numeric_columns = ["year", "revenue", "profit", "employees", "users"]

for column in numeric_columns:
    annual[column] = pd.to_numeric(
        annual[column],
        errors="coerce"
    )

# Remove rows without a valid year.
annual = annual.dropna(subset=["year"]).copy()

# Remove rows where all measured variables are missing.
measurement_columns = ["revenue", "profit", "employees", "users"]

annual = annual.dropna(
    subset=measurement_columns,
    how="all"
).copy()

# Convert year to integer.
annual["year"] = annual["year"].astype(int)

# Sort observations chronologically.
annual = annual.sort_values("year").reset_index(drop=True)

print("Shape:", annual.shape)
print("\nMissing values:")
display(annual.isna().sum())

display(annual)

# %% [markdown]
# ## 2. Aaliza Statystyczna
#
# W kolejny etapie przeprowadzono analizę statystyczną zmiennych opisujących przychody, zysk, zatrudnienie oraz liczbę użytkownikóœ.
#
# Celem jest określenie podstawowaych właściowści statystycznycch oraz identyfikacja nietypowych obserwacji.

# %%
variables = ["revenue", "profit", "employees", "users"]

descriptive_stats = annual[variables].describe()

display(descriptive_stats)

# %%
