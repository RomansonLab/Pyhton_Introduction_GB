# Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

import pandas as pd

data = pd.read_csv('california_housing_train.csv')

min_population = 0
max_population = 500

res = data[(data['population'] >= min_population) & (data['population'] <= max_population)]['median_house_value']
print(res)