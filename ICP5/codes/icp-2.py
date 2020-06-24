from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

train = pd.read_csv(Path('./winequality-red.csv'))



# Working with Numeric Features
n_features = train.select_dtypes(include=[np.number])
corr = n_features.corr()
print('The top 3 correlated features \n')
print(corr['quality'].sort_values(ascending=False)[:3], '\n')

# negative correlated features
print('The top 3 negative correlated features \n')
print(corr['quality'].sort_values(ascending=False)[-3:], '\n')

# Null values
nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False))
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

# #handling missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()
print('The values without 0 sum',sum(data.isnull().sum() != 0))

# Build a linear model
y = np.log(train.quality)
X = data.drop(['quality'], axis=1)

#Train test split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)


lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

# Evaluate the performance,R2 and RMSE
print("R^2 is: ", model.score(X_test, y_test))
predictions = model.predict(X_test)


print('RMSE is: ', mean_squared_error(y_test, predictions))
