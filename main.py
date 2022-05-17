import pandas as pd

heart_data = pd.read_csv('heart.csv')
heart_data.head()
heart_data.tail()
heart_data.shape
heart_data.isnull().sum()
heart_data.describe()
heart_data['target'].value_counts()

X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']
print(X)
print(Y)
