#from keras.models import Sequential
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras import optimizers

csv_table = np.genfromtxt('input.csv', delimiter=',')
#model = Sequential()
print(csv_table.shape)
#get input columns from table
inarr=csv_table[:,[0]]

#get output columns from table
outarr=csv_table[:,[1]]

print(inarr.shape)
print(outarr.shape)

model=Sequential()
#hidden layer1
model.add(Dense(units=3, activation='sigmoid', input_dim=1))
#output layer
model.add(Dense(units=1, activation='sigmoid'))
print(model.summary())

#use sgd or adagrad as optimizer
sgd=optimizers.SGD(lr=1)
#use binary_crossentropy as loss function because it works well with binary classification(fraud or not fraud)
model.compile(loss='binary_crossentropy', optimizer=sgd)

#Start the training
model.fit(inarr, outarr, epochs=1500, verbose=False)

#after training, let's predict
predict_amt=np.array([54134,60000, 500, 49000, 65643, 91123])

print(model.predict(predict_amt))