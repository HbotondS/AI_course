from glob import glob
import cv2
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


def train(training_inputs, training_outputs, training_iterations, weights):

    for iteration in range(training_iterations):

        inputs = inputs.astype(float)
        output = sigmoid(np.dot(inputs, weights))

        error = training_outputs - output

        adjustments = np.dot(training_inputs.T, error * sigmoid_derivative(output))

        weights += adjustments


def Offline_learning(inputs, outputs_expected, activation_func, gradf, learning_rate):

    size_input = len(inputs[0])

    weights = np.random.randn(size_input)

    weights.shape = (size_input, 1)

    epoch = 0

    while True:

        value = np.dot(inputs, weights)
        output = activation_func(value)
        current_error = np.subtract(output, outputs_expected)
        x_transpose = np.transpose(inputs)
        grad_value = gradf(value)
        grad_value.shape = (len(grad_value), 1)
        something = np.dot(current_error, grad_value)
        g = np.dot(x_transpose, something)
        weights = np.subtract(weights, (learning_rate * g))
        E = sum_column_square(current_error)

        if E < 0.00001 or epoch > 5000:
            break

        epoch += 1


def sum_column_square(element):
    length = len(element)
    summ = 0

    for i in range(length):
        summ += element[i] ** 2

    return summ


def v_gradf(x):
    length = len(x)

    for i in range(length):
        x[i][0] = sigmoid_derivative(x[i][0])
    return np.array(x, dtype=float)


if __name__ == "__main__":

    images_elephant = []
    images_starfish = []

    for image in glob("./elephant/*.jpg"):
        im = cv2.imread(image, 0)
        images_elephant.append(im)

    for image in glob("./starfish/*.jpg"):
        im = cv2.imread(image, 0)
        images_starfish.append(im)

    images = images_elephant + images_starfish
    outputs_expected = np.concatenate( (np.zeros(len(images_elephant)), np.ones(len(images_starfish))), axis=0 )
    Offline_learning(images[0], outputs_expected[0], sigmoid, v_gradf, 0.00005)
