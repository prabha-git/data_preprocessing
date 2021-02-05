import pandas as pd
import feather
import re
from datetime import datetime as dt

#reading unclean data
data = pd.read_feather("../data/covid.ftr")

# Convert these column to int data type
col = ['cases','deaths','recovered']
data[col] = data[col].apply(lambda x: pd.to_numeric(x,errors='coerce').astype('Int64'),axis=0)

# To remove the subscript text
data['country'] = data['country'].apply(lambda x:re.sub(r'\[.*\]','',x))
data['updated_ts']=pd.Series([dt.now()]*len(data))

data.to_csv("test.csv")