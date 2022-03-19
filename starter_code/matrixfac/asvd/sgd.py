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
        batch_size (int): Size of the batch to use on each iteration of stochastic gradient descent (how many examples to approximate derivative with).
        num_iter (int): The number of iterations to train the model for (each iteration consists of a single weight update)
        learning_rate (float): Controls the magnitude of each weight update
    """
    # grab the batch size for easier computation later
    B = X_train.shape[1]
    # We are looping for num_iter iterations and updating the input every step
    for i in range(num_iter):
        # Here we choose the B indices that form our stochastic batch
        indices = np.random.randint(0, B, (batch_size))
        # Getting the inputs and labels (output values) at the indices in B
        batched_inputs, batched_labels = X_train[indices], y_train[indices]
        # Computing the loss on this batch of inputs
        loss = model.loss(batched_inputs, batched_labels, grad=True)
        if i % 250 == 0:
            print(f"Iteration {i}: training loss = {loss}")
        # Performing weight update. zip allows us to iterate through multiple equal sized lists/tuples at once!
        for param, grad in zip(model.parameters(), model.grad()):
            param -= learning_rate * grad
