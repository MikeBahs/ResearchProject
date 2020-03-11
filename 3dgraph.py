from dataset import allFramesFiltered as df
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as py
import numpy as np
import traceback
import time

zAxis = []
yAxis = []
i = 0
length = len(df)

try:

    # here we concatinate set of arrays using numpy to display they in the graph
    allAvg = np.concatenate((df['Avg']), axis=0)
    allYears = np.concatenate((df['Year']), axis=0)
    allStocs = np.concatenate((df['Stock']), axis=0)

    # minValueAvg = min(allAvg)
    # maxValueAvg = max(allAvg)
    start = time.time()
    # print("Time taken to build plot")
    # for ind, type in enumerate(df['Stock']):
    #     start = time.time()
    #     print("Time taken to go through one Stock and put it on a plot")
    #     for i, z in enumerate(df['Avg'][ind]):
    #         x = allAvg[i]
    #         y = allYears[i]
    #         plt.scatter(x, y, alpha=0.5, marker='D', color='green')
    #         plt.text(x + 0.1, y + 0.1, type, fontsize=4)
    #         end = time.time()
    #         print(end - start)
    # plt.xlabel('Year')
    # plt.ylabel('Average Adjustment Close Price')
    # plt.title('Stock market graph')
    # plt.legend()
    # # show plot right away
    # plt.show()
    end = time.time()
    print(end - start)
    # save plot as pdf file
    # plt.savefig('plot.pdf')

    # for ind, type in enumerate(df['Stock']):
    #     for i, z in enumerate(df['Avg']):
    #         # x = allAvg[i]
    #         # y = allYears[i]
    #         # z = allStocs[i]

    df = pd.DataFrame(dict(year=allYears[1], avgPrice=allAvg[1],
                           stocks=allStocs[1]), index=[1])

    # Use column names of df for the different parameters x, y, color, ...
    fig = py.scatter(df, x="year", y="avgPrice", color="stocks",
                     title="Stock market graph",
                     labels={"avgPrice": "Price in USD"}  # customize axis label
                     )

    fig.show()

except Exception as e:
    print(traceback.format_exc())
