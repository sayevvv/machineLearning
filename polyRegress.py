import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data2.csv', delimiter=',', skip_header=1)

x = data[:, 0]
y = data[:, 1]

polyModel = np.poly1d(np.polyfit(x, y, 3))

myline = np.linspace(1, 10, 100)

plt.scatter(x, y)
plt.title("Polynomial Regression")
plt.xlabel("this is x")
plt.ylabel("this is y")
plt.plot(myline, polyModel(myline), c='hotpink')
plt.show()