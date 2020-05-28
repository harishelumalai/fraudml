#from keras.models import Sequential
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras import optimizers

csv_table = np.genfromtxt('input2.csv', delimiter=',')
print(csv_table.shape)
#get input columns from table
inarr=csv_table[:,[0,1]]

#get output columns from table
outarr=csv_table[:,[2]]

model=Sequential()
#hidden layer1
model.add(Dense(units=4, activation='relu', input_dim=2))
model.add(Dense(units=2, activation='relu'))
#output layer
model.add(Dense(units=1, activation='sigmoid'))
print(model.summary())

#use sgd or adagrad as optimizer
sgd=optimizers.SGD(lr=1)
adagrad=optimizers.Adagrad()
#use binary_crossentropy as loss function because it works well with binary classification(fraud or not fraud)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#after training, let's predict
predict_arr=np.array([[541.34,0],[600.00,7], [5.00,6], [5.00,0], [490.00,2], [656.43,1], [911.23,0]])
print( predict_arr.shape)

#Start the training
model.fit(inarr, outarr, epochs=150, verbose=True, batch_size=20)

print(model.get_weights())
print(model.predict(predict_arr))
# evaluate the keras model
_, accuracy = model.evaluate(inarr, outarr)
print('Accuracy: %.2f' % (accuracy*100))