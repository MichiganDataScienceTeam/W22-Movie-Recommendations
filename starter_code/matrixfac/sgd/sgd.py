from trainable import Trainable
import numpy as np


def sgd(
    model,
    X_train,
    y_train,
    batch_size,
    num_iter,
    learning_rate,
):
    """
    Trains the given model on the input data using stochastic gradient descent

    Args:
        model (Trainable): A trainable machine learning model. See the Trainable module for details.
        X_train (np.ndarray): Input training data. Matrix of size (N,D) where N is the number of examples.
        y_train (np.ndarray): Ground truth values for inputs in training data. Vector of size (N) where N is the number of examples.
        batch_size (int): Size of the batch to use on each iteration of stochastic gradient descent.
        num_iter (int): The number of iterations to train the model for (each iteration consists of a single weight update)
        learning_rate (float): Controls the magnitude of each weight update
    """
    # your implementation here!
    pass
