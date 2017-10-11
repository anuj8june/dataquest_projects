import pandas as pd

data = pd.read_csv("data_files/CRDC2013_14.csv",encoding="Latin-1")
print(data["JJ"].value_counts())
print("#############################")
print(data["SCH_STATUS_MAGNET"].value_counts())
print("#############################")
print(pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum"))
print("#############################")
print(pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum"))

