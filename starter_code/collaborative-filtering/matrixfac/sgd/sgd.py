from trainable import Trainable
import numpy as np


def sgd(
    model: Trainable,
    X_train: np.ndarray,
    y_train: np.ndarray,
    batch_size: int,
    num_iter: int,
    learning_rate: float,
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
    losses = []
    B = X_train.shape[1]
    for i in range(num_iter):
        indices = np.random.randint(0, B, (batch_size))
        batched_inputs, batched_labels = X_train[indices], y_train[indices]
        loss = model.loss(batched_inputs, batched_labels, grad=True)
        losses.append(loss)
        # val_loss = model.loss(X_test, y_test)
        # val_losses.append(val_loss)
        if i % 250 == 0:
            print(f"Iteration {i}: training loss = {loss}")
        for param, grad in zip(model.parameters(), model.grad()):
            param -= learning_rate * grad
