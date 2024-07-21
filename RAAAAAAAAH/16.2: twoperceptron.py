import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import to_categorical

linearSeparableFlag = True
x_bias = 0

def toy_2D_samples(x_bias ,linearSeparableFlag):
    if linearSeparableFlag:
        samples1 = np.random.multivariate_normal([5+x_bias, 5], [[1, 0],[0, 1]], 50)
        samples2 = np.random.multivariate_normal([-5+x_bias, -5], [[1, 0],[0, 1]], 50)
        samples3 = np.random.multivariate_normal([-5+x_bias, 5], [[1, 0],[0, 1]], 50)
        samples4 = np.random.multivariate_normal([5+x_bias, -5], [[1, 0],[0, 1]], 50)

        samples = np.concatenate((samples1, samples2, samples3, samples4 ), axis =0)
    
        # Plot the data
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'bo')
        plt.plot(samples3[:, 0], samples3[:, 1], 'rx')
        plt.plot(samples4[:, 0], samples4[:, 1], 'rx')
        plt.show()

    else:
        samples1 = np.random.multivariate_normal([5+x_bias, 5], [[1, 0],[0, 1]], 50)
        samples2 = np.random.multivariate_normal([-5+x_bias, -5], [[1, 0],[0, 1]], 50)
        samples3 = np.random.multivariate_normal([-5+x_bias, 5], [[1, 0],[0, 1]], 50)
        samples4 = np.random.multivariate_normal([5+x_bias, -5], [[1, 0],[0, 1]], 50)

        samples = np.concatenate((samples1, samples2, samples3, samples4 ), axis =0)
    
        # Plot the data
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'rx')
        plt.plot(samples3[:, 0], samples3[:, 1], 'bo')
        plt.plot(samples4[:, 0], samples4[:, 1], 'rx')
        plt.show()

    labels = assign_labels(samples)
    return samples, labels

def assign_labels(samples):
    new_labels = []
    for sample in samples:
        if (sample[0] >= 0 and sample[1] >= 0) or (sample[0] <= 0 and sample[1] <= 0):
            new_labels.append([1, 0])  # Blue
        else:
            new_labels.append([0, 1])  # Red
    return np.array(new_labels)

samples, labels = toy_2D_samples(x_bias ,linearSeparableFlag)

# Convert labels to one-hot encoding
labels = to_categorical(labels[:, 0])  # Only take the first column for binary labels

# Split training and testing set
randomOrder = np.random.permutation(len(samples))
trainingX = samples[randomOrder[0:100],:]
trainingY = labels[randomOrder[0:100]]
testingX = samples[randomOrder[100:200],:]
testingY = labels[randomOrder[100:200]]

# Build the model
model = Sequential()
model.add(Dense(8, input_shape=(2,), activation='relu', use_bias=False))  # Two perceptrons
model.add(Dense(8, activation='relu'))  # Two perceptrons
model.add(Dense(2, activation='softmax'))  # Two perceptrons
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.fit(trainingX, trainingY, epochs=100, batch_size=10, verbose=1, validation_split=0.2)

# score = model.evaluate(testingX, testingY, verbose=0)
score = 0
for i in range(len(testingX)):
    output = model.predict(np.array([testingX[i,:]]))
    estimate = np.argmax(output)  # Get the index of the max value

    if estimate == 0:
        plt.plot(testingX[i, 0], testingX[i, 1], 'rx')
    else: 
        plt.plot(testingX[i, 0], testingX[i, 1], 'bo')

    if estimate == np.argmax(testingY[i]):
        score = score  + 1

plt.show()
print('Test accuracy:', score/100)
