import pandas as pd
import glob
from statistics import mean

directory = 'data'
pd.set_option("display.precision", 2)

# Creating dataset

all_files = glob.glob(directory + "/*.csv")

li = []
liYear = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df['Date'] = pd.to_datetime(df['Date'])
    stockname = str(filename)[5:-4]
    df.insert(0, 'Stock', stockname)

    #print(df.info())

    # Parsing
    lYear = {
        'Stock': [],
        'Year': [],
        'Avg': []
    }

    temp = {}
    y = 2012
    while y > 1999:
        temp[y] = []
        for line in df['Date'].dt.year:
            if line == y:
                for adjClose in df['Adj Close']:
                    temp[y].append(adjClose)
            continue

        lYear['Year'].append(y)
        lYear['Stock'].append(stockname)
        lYear['Avg'].append(mean(temp[y]))
        y -= 1

    print("Stocks")
    for s in lYear['Stock']:
        print(s)
    print("Year")
    for y in lYear['Year']:
        print(y)
    print('Avg')
    for avg in lYear['Avg']:
        print(avg)

    li.append(df)

ds = pd.concat(li, axis=0, ignore_index=True)
# ds['Date'] = pd.to_datetime(ds['Date'])

# print(ds.head())

# print(ds['Date'].dt.year)

# print(ds.info())
