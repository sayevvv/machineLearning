import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)

x = data[:, 0]
y = data[:, 1]

slope, intercept, r, p, std_err = stats.linregress(x, y) #linear regression


def myfunc(x): #y = mx + c
    return slope * x + intercept

model = list(map(myfunc, x))

plt.scatter(x, y, c='red')
plt.plot(x, model)
plt.show()