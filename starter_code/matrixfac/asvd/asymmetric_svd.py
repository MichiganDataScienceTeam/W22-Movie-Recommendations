from trainable import Trainable
import numpy as np


class AsymmetricSVD(Trainable):
    def __init__(self):
        """
        Class constructor. Modify any part of this function (parameters, content, etc!)
        """
        pass

    def predict(self, R):
        """
        Predicts the output ratings given the input partial rating matrix.

        Args:
            R (np.ndarray): Partial rating matrix of size (B, M) where B is the size of
                            the batch, and M is the number of ratings per user.

        Returns:
            pred (np.ndarray): Output matrix of size (B, M) giving fully filled rating matrix prediction
        """
        pass

    def parameters(self):
        """
        Returns the parameters of the model

        Returns:
            Tuple: The set of model parameters (Z, V)
        """
        pass

    def loss(self, R, grad=False) -> np.float64:
        """
        Determines the loss of the model when run on input partial rating matrix R.

        Args:
            R (np.ndarray): Partial rating matrix of size (B, M) where B is the size of
                            the batch, and M is the number of ratings per user.
            grad (bool, optional): Enables caches for gradient computation. Defaults to False. If true,
                                   the model will track gradients of parameters with respect to the loss
                                   value on input R.

        Returns:
            np.float64: Loss of the model
        """
        pass

    def grad(self):
        """
        Returns the gradients of the model parameters after the previous call to loss()

        Returns:
            Tuple: set of gradients for all model parameters (gradient for Z, gradient for V)
        """
        pass

    def update_parameters(self, Z, V):
        """
        Updates model parameters to new values

        Args:
            Z (np.ndarray): Updated value for Z
            V (np.ndarray): Updated value for V
        """
        pass
