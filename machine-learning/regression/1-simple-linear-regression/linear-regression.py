"""
This file contains a small implementation of a simple univariate linear regression
"""
import random

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression


class LinearRegression:
    def __init__(self, x, y, epochs: int = 100, lr: float = 0.001):
        """

        :param numpy.ndarray x: the feature vector with shape (n, 1).
        :param numpy ndarray y: the dependent variable vector with shape (n, ).
        :param int epochs: number of epochs to converge. Defaults to 100.
        :param float lr: the value of the learning rate. Defaults to 0.001.
        """
        self.x = x
        self.y = y
        self.beta0 = random.random()
        self.beta1 = random.random()
        self.epochs = epochs
        self.lr = lr

    def fit(self):
        for i in range(self.epochs):

            if i % 25 == 0:
                self._plot_line()

            self._update_parameters()
        self._plot_line()

    def _update_parameters(self):
        d_beta0, d_beta1 = self._derivatives()
        self.beta0 = self.beta0 - self.lr * d_beta0
        self.beta1 = self.beta1 - self.lr * d_beta1

    def _derivatives(self):
        d_beta0 = 0
        d_beta1 = 0
        for (xi, yi) in zip(self.x, self.y):
            d_beta0 += (self.beta0 + self.beta1 * xi) - yi
            d_beta1 += ((self.beta0 + self.beta1 * xi) - yi) * xi
        return d_beta0, d_beta1

    def _plot_line(self):
        max_x = max(self.x)
        min_x = min(self.x)
        x_plot = np.linspace(min_x, max_x, 100)
        y_plot = self.beta0 + self.beta1 * x_plot

        plt.plot(x_plot, y_plot, color="red", label="Regression line")
        plt.scatter(self.x, self.y)
        plt.show()


if __name__ == "__main__":
    seed = 42
    random.seed(seed)
    x, y = make_regression(
        n_samples=100, n_features=1, noise=10, bias=1, random_state=seed
    )
    linear = LinearRegression(x, y)
    linear.fit()
    print(linear.beta0, linear.beta1)
