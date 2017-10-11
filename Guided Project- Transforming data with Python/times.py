import read
import pandas as pd
from dateutil.parser import parse


df = read.load_data()

def hour_ext(stmp):
    dates = parse(stmp)
    return dates.hour

df["hour"] = df["submission_time"].apply(hour_ext)
print(df["hour"].value_counts())