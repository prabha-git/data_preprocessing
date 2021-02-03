import pandas as pd
import feather

data = pd.read_feather("../data/covid.ftr")

col = ['cases','deaths','recovered']

data[col] = data[col].apply(lambda x: pd.to_numeric(x,errors='coerce').astype('Int64'),axis=0)

data.to_csv("test.csv")