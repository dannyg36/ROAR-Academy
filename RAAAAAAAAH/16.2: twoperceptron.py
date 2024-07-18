# Load dependencies
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

# Create data
linearSeparableFlag = False
x_bias = 6

def toy_2D_samples(x_bias, linearSeparableFlag):
    if linearSeparableFlag:
        samples1 = np.random.multivariate_normal([5 + x_bias, 0], [[1, 0], [0, 1]], 100)
        samples2 = np.random.multivariate_normal([-5 + x_bias, 0], [[1, 0], [0, 1]], 100)
        samples = np.concatenate((samples1, samples2), axis=0)
    else:
        samples1 = np.random.multivariate_normal([5 + x_bias, 5], [[1, 0], [0, 1]], 50)
        samples2 = np.random.multivariate_normal([-5 + x_bias, -5], [[1, 0], [0, 1]], 50)
        samples3 = np.random.multivariate_normal([-5 + x_bias, 5], [[1, 0], [0, 1]], 50)
        samples4 = np.random.multivariate_normal([5 + x_bias, -5], [[1, 0], [0, 1]], 50)
        samples = np.concatenate((samples1, samples2, samples3, samples4), axis=0)
    return samples

samples = toy_2D_samples(x_bias, linearSeparableFlag)

def assign_labels(samples):
    new_labels = []
    for sample in samples:
        if (sample[0] > 0 and sample[1] > 0) or (sample[0] < 0 and sample[1] < 0):
            new_labels.append([1, 0])  # Blue
        else:
            new_labels.append([0, 1])  # Red
    return np.array(new_labels)

new_labels = assign_labels(samples)

# Split training and testing set
randomOrder = np.random.permutation(200)
trainingX = samples[randomOrder[0:100], :]
testingX = samples[randomOrder[100:200], :]
trainingY = new_labels[randomOrder[0:100], :]
testingY = new_labels[randomOrder[100:200], :]

# Build the model
model = Sequential()
model.add(Dense(2, input_shape=(2,), activation='sigmoid'))  # Two perceptrons
model.add(Dense(2, activation='softmax'))  # Output layer
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['binary_accuracy'])

# Train the model
model.fit(trainingX, trainingY, epochs=500, batch_size=10, verbose=1, validation_split=0.2)

# Evaluate and plot the results
score = 0
for i in range(100):
    predict_x = model.predict(np.array([testingX[i, :]]))
    estimate = np.argmax(predict_x, axis=1)

    if testingY[i, estimate] == 1:
        score += 1

    if estimate == 0:
        plt.plot(testingX[i, 0], testingX[i, 1], 'bo')
    else:
        plt.plot(testingX[i, 0], testingX[i, 1], 'rx')

print('Test accuracy:', score / 100)
plt.show()
