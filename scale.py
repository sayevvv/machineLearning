import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

db = pd.read_csv('exercise_data.csv')

x = db[["Duration", "Pulse", "Maxpulse"]]
standardized = StandardScaler().fit_transform(x)

print(standardized)

plt.plot(x)
plt.show()