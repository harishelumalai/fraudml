#from keras.models import Sequential
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras import optimizers

csv_table = np.genfromtxt('other_ctry_cnt.csv', delimiter=',')
print(csv_table.shape)
#get input columns from table
inarr=csv_table[:,[0,1]]

#get output columns from table
outarr=csv_table[:,[2]]

model=Sequential()
#hidden layer1
model.add(Dense(units=3, activation='sigmoid', input_dim=2))
#model.add(Dense(units=2, activation='relu'))
#output layer
model.add(Dense(units=1, activation='sigmoid'))
print(model.summary())

#use sgd or adagrad as optimizer
sgd=optimizers.SGD(lr=1)
adagrad=optimizers.Adagrad()
#use binary_crossentropy as loss function because it works well with binary classification(fraud or not fraud)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


#Start the training
model.fit(inarr, outarr, epochs=150, verbose=True)

#after training, let's predict
predict_arr=np.array([[0,0],[1,0],[0,1],[1,1]])
print( predict_arr.shape)

print(model.get_weights())
print(model.predict(predict_arr))
# evaluate the keras model
_, accuracy = model.evaluate(inarr, outarr)
print('Accuracy: %.2f' % (accuracy*100))

[print(str(round(i[0]))) for i in predict_out]

print(model.get_weights())

model.save('other_ctry_cnt_model', include_optimizer=True)