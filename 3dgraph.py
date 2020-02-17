from dataset import ds
import matplotlib.pyplot as plt

x = ds['Low']
y = ds['High']

plt.plot(x, y, label = str(ds['stock']))

# for line in ds.head():
#     x = line['Low']
#     y = line['High']
#
#     plt.plot(x, y, label = str(line['stock']))

plt.xlabel('Date Label')
plt.ylabel('High Label')
plt.title('Stock market graph')
plt.legend()
plt.show()