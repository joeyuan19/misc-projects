from ys import *
import matplotlib.pyplot as plt

data = get_historical_prices("msft","20130101","20140101")

x = []
y = []
for day in data:
    x.append(day[0])
    y.append(day[1])



plt.plot([i for i in range(len(x))],y)
plt.show()
