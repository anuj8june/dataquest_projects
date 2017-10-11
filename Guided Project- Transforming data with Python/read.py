import pandas as pd

def load_data():
    
    data = pd.read_csv("hn_stories.csv")

    data.columns = ['submission_time', 'upvotes', 'url', 'headline']

    #print(data.columns.values)
    #print(data.head(1))
    
    return data