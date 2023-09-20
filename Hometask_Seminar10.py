# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_categories = data['whoAmI'].unique()

# создаем новые столбцы
for category in unique_categories:
    data[category] = (data['whoAmI'] == category).astype(int)

# далее удаляю столбец whoAmI из data, т.к. поидее больше не нужен
# inplace=True - операция удаления должна быть выполнена в текущем объекте data, а не создавать новый объект

data.drop(columns=['whoAmI'], inplace=True)
print(data.head())
