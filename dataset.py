import pandas as pd
import glob
from statistics import mean

# Initialize two lists and add frames to them later while iterating through stocks
allStockDataFrames = []
stockWithSelectedData = []

# Iterating through files in data folder
directory = 'data'
pd.set_option("display.precision", 2)
all_files = glob.glob(directory + "/*.csv")

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df['Date'] = pd.to_datetime(df['Date'])
    stockname = str(filename)[5:-4]
    df.insert(0, 'Stock', stockname)

    # Parsing
    # Creating an array for each Stock by year
    lYear = {
        'Stock': [],
        'Year': [],
        'Avg': []
    }
    # Add stock name to the stocks
    lYear['Stock'].append(stockname)

    # Loop through years and add Year and Avg Adjustment Close to the list
    year = 2012
    while year > 1999:
        # Add Avg Adjustment Close price to the list using df.loc function
        # check if dataframe is not empty for a specific year
        if not df.loc[df['Date'].dt.year == year, 'Adj Close'].empty:
            lYear['Avg'].append(mean(df.loc[df['Date'].dt.year == year, 'Adj Close']))
            lYear['Year'].append(year)
            print(f'Average for {stockname} in year {year} is {lYear["Avg"][-1]}')
        year -= 1  # decrease counter

    stockWithSelectedData.append(lYear);
    allStockDataFrames.append(df)

# Concatenate all the results together
# this lines combines all the dataframes of all token with no filters
allFrames = pd.concat(allStockDataFrames, axis=0, ignore_index=True)

# this lines combines all the dataframes with filters (Avg, Year, StockName)
allFramesFiltered = pd.DataFrame(stockWithSelectedData)
