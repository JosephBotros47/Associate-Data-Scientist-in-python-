import numpy as np
import pandas as pd

df = pd.read_csv("DRSharp_20260721_184823Z_SNR.csv")
for lab,row in df.iterrows():
    print(lab)
    print(row)