import pandas as pd

def null_filler(col):
    if col.dtype!='object':
        col=col.fillna(col.median())
    else:
        col=col.fillna(col.mode())
    return col



def encoder(col):
    encoded=pd.get_dummies(col,drop_first=True)
    return encoded