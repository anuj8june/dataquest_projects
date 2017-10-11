import pandas as pd
contents = pd.read_csv("CRDC2013_14content.csv")
print(contents.head())
print("########################################")
print(contents.columns.values)