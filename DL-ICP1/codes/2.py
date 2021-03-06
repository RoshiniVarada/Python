import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
dataset = pd.read_csv('breastcancer.csv')
X=dataset.iloc[:,2:31].values
Y=dataset.iloc[:,1].values
labelencoder_Y = LabelEncoder()
Y= labelencoder_Y.fit_transform(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.25, random_state=87)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(40, input_dim=29, activation='relu')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))
