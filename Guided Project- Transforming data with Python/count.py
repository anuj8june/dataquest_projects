import read
import pandas as pd
from collections import Counter

df = read.load_data()
print(df.head(2))
long_str = ' '.join(df['headline'].astype(str).tolist())
str_list = long_str.split(' ')

cnt = Counter()
for word in str_list:
    cnt[word] += 1
    
for val in cnt:
    if cnt[val] > 100:
        print(val)