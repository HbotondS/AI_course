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


if __name__ == "__main__":

    images_elephant = []
    images_starfish = []

    weights = 2 * np.random.random((3, 1)) - 1

    for image in glob("D:/101_ObjectCategories/elephant/*.jpg"):
        im = cv2.imread(image)
        grayImage = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        images_elephant.append(grayImage)

    for image in glob("D:/101_ObjectCategories/starfish/*.jpg"):
        im = cv2.imread(image)
        grayImage = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        images_starfish.append(grayImage)