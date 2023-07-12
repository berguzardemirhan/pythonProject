import pandas as pd

data = pd.read_csv(r"C:/Users/lenovo/PycharmProjects/pythonProject/odev2/Iris.csv",)

data.loc[data['species'] == 'Iris-setosa', 'species'] = 'manolya'
data.loc[data['species'] == 'Iris-versicolor', 'species'] = 'gül'
data.loc[data['species'] == 'Iris-virginica', 'species'] = 'lale'

data.to_excel(r"C:/Users/lenovo/PycharmProjects/pythonProject/odev2/Dataset.xlsx")