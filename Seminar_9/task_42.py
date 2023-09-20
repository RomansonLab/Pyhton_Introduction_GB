# Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

data = pd.read_csv('california_housing_train.csv')

res = data[data['population'] == data['population'].min()]['households'].max()
print(res)

