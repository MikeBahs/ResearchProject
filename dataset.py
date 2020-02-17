import pandas as pd
import glob

directory = 'data'
pd.set_option("display.precision", 2)

#Creating dataset

all_files = glob.glob(directory + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    stockname = str(filename)[5:-4]
    df.insert(0, 'stock', stockname)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

print(frame.head())