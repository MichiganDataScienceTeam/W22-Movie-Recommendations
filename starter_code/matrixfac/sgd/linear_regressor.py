from trainable import Trainable
import numpy as np


class LinearRegressor(Trainable):
    def __init__(self, N, reg):
        """
        Creates a linear regressor that predicts a single float value from
        a vector of inputs with size D

        Args:
            D (int): Vector size of inputs to the model
            reg (int): Regularization parameter
        """
        self.W = 0.001 * np.random.randn(N)
        self.bias = 0.001 * np.random.randn(1)
        self.reg = reg

    def predict(self, X):
        """
        Predicts a set of float values given a batch of inputs

        Args:
            X (np.ndarray): Inputs of size (N, D) where N is the size of the batch

        Returns:
            y (np.ndarray): Output vector of size (N) giving predictions for each input
        """
        return X @ self.W + self.bias

    def parameters(self):
        """
        Returns the parameters of the model

        Returns:
            Tuple: The set of model parameters (weights, bias)
        """
        return self.W, self.bias

    def loss(self, X, y, grad=False) -> np.float64:
        """
        Determines the loss of the model when run on inputs X with ground truths y.

        Args:
            X (numpy.ndarray): Batch of model inputs
            y (numpy.ndarray): Batch of ground truths per model inputs
            grad (bool, optional): Enables caches for gradient computation. Defaults to False.

        Returns:
            np.float64: Loss of the model
        """
        pred = self.predict(X)
        error = 0.5 * np.sum((y - pred) ** 2) / X.shape[0]  # mean squared error
        error += 0.5 * self.reg * np.sum(self.W * self.W)  # L2 regularization
        if grad:
            self.cache = (X, y, pred)
        return error

    def grad(self):
        """
        Returns the gradients of the model parameters after the previous call to loss()

        Returns:
            Tuple: set of gradients for all model parameters (gradient for weights, gradient for bias)
        """
        X, y, pred = self.cache
        self.W_grad = (
            -1 * np.sum((y - pred) * X.T, axis=1) / X.shape[0]
            + self.reg * self.W
        )
        self.b_grad = -1 * np.sum(y - pred) / X.shape[0]
        return self.W_grad, self.b_grad

    def update_parameters(self, weights, bias):
        """
        Updates model parameters to new values

        Args:
            weights (np.ndarray): new weight value
            bias (np.ndarray): new bias value
        """
        self.W = weights
        self.bias = bias
