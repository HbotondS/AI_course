import numpy as np

input_array = np.array([
    [1, 0, 1,
     1, 1, 1,
     1, 0, 1, 1],  # H
    [1, 1, 1,
     0, 1, 0,
     1, 1, 1, 0],  # I
])

output_array = np.array([
    [1, 0],
    [0, 1],
])


def hard_lim(val):
    if val < 0:
        return 0
    else:
        return 1


def perceptron_learning(data, expected_output):
    N, n = data.shape
    lr = .1
    w1 = np.random.randn(n, 1)
    w2 = np.random.randn(n, 1)

    E = 1

    while E != 0:
        E = 0

        for i in range(N):
            yi1 = hard_lim(np.dot(data[i], w1))
            yi2 = hard_lim(np.dot(data[i], w2))

            ei1 = expected_output[i][0] - yi1
            ei2 = expected_output[i][1] - yi2

            w1 += lr * ei1 * data[i].reshape(n, 1)
            w2 += lr * ei2 * data[i].reshape(n, 1)

            E += ei1 ** 2
            E += ei2 ** 2


perceptron_learning(input_array, output_array)
