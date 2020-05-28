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
print("input")
print(inarr)
print(outarr.shape)
print("output")
print(outarr)

model=Sequential()
#hidden layer1
model.add(Dense(units=2, activation='sigmoid', input_dim=1))
#output layer
model.add(Dense(units=1, activation='relu'))
print(model.summary())

#use sgd or adagrad as optimizer
sgd=optimizers.SGD(lr=1)
adagrad=optimizers.Adagrad()
#use binary_crossentropy as loss function because it works well with binary classification(fraud or not fraud)
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

#after training, let's predict
predict_amt=np.array([[54134],[60000], [500], [49000], [65643], [91123]])
print( predict_amt.shape)

#Start the training
model.fit(inarr, outarr, epochs=250, verbose=True, batch_size=10)

print(model.get_weights())
print(model.predict(predict_amt))