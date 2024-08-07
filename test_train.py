import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = np.poly1d(np.polyfit(train_x, train_y, 3))

myline = np.linspace(0, 6, 100)

plt.scatter(train_x, train_y, label='Train Data')
plt.scatter(5, mymodel(5), color='red', label=f'mymodel(5) = {mymodel(5):.2f}')
plt.plot(myline, mymodel(myline), color='blue', label='Model Line')
plt.legend()
plt.show()