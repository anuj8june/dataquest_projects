import read
import pandas as pd

df = read.load_data()
urls = df["url"].value_counts()
print_urls = urls >= 100
url_out = urls[print_urls]
print(url_out)

