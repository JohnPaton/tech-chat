# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # CoolBlue Data Exploration

# %%
from pathlib import Path
import pandas as pd

# %%
pd.options.display.max_columns = 25
pd.options.display.max_colwidth = 999

# %%
root = Path.cwd().parent
data = root / "data"

# %%
df = pd.read_csv(data / "raw" / "coolblue_mobiele_telefoons_feed.csv")

# %%
df.sample(5)

# %%
import requests

# %%
requests.get("https://www.coolblue.nl/product/871087", user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36
")

# %%
