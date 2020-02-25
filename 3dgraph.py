from dataset import allFramesFiltered as ds
import matplotlib.pyplot as plt

x = ds.head['Year']
y = ds.head['Avg']

plt.plot(x, y)

plt.xlabel('Year')
plt.ylabel('Average Adjustment Close Price')
plt.title('Stock market graph')
plt.legend()
plt.show()
