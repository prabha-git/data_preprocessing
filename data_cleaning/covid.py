import sys
import pandas as pd
import feather
import re
from datetime import datetime as dt




def clean_data(df):

    # Convert these column to int data type
    col = ['cases','deaths','recovered']
    df[col] = df[col].apply(lambda x: pd.to_numeric(x,errors='coerce').astype('Int64'),axis=0)

    # To remove the subscript text
    df['country'] = df['country'].apply(lambda x:re.sub(r'\[.*\]','',x))
    df['updated_ts']=pd.Series([dt.now()]*len(df))

    return df
    