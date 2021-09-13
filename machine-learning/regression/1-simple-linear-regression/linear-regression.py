import random
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression


class LinearRegression:
    def __init__(self, x, y, epochs: int = 1000, lr: float = 0.001):
        self.x = x
        self.y = y
        self.beta0 = random.random()
        self.beta1 = random.random()
        self.epochs = epochs
        self.lr = lr

    def fit(self):
        for i in range(self.epochs):
            if i % 100 == 0:
                self.plot_line()

            self.update_parameters()

    def update_parameters(self):
        d_beta0, d_beta1 = self.derivatives()
        self.beta0 = self.beta0 - self.lr * d_beta0
        self.beta1 = self.beta1 - self.lr * d_beta1

    def derivatives(self):
        d_beta0 = 0
        d_beta1 = 0
        for (xi, yi) in zip(self.x, self.y):
            d_beta0 += (self.beta0 + self.beta1 * xi) - yi
            d_beta1 += ((self.beta0 + self.beta1 * xi) - yi) * xi
        return d_beta0, d_beta1

    def plot_line(self):
        max_x = max(self.x) + 100
        min_x = min(self.x) - 100


if __name__ == "__main__":
    seed = 42
    random.seed(seed)
    x, y, coef = make_regression(
        n_samples=100, n_features=1, noise=0.02, bias=2, random_state=seed, coef=True
    )
    print(x.shape)
    print(y.shape)
    print(coef)
    lr = LinearRegression(x, y)
    lr.fit()
    print(lr.beta0, lr.beta1)
