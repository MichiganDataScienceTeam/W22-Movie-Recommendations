import abc
import numpy


class Trainable(abc.ABC):
    """
    An abstract base class for trainable ML algorithms
    """

    def parameters(self):
        """
        Returns the parameters of the model

        Raises:
            NotImplementedError: Raised if this function is not overridden by subclasses.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def loss(self, X, y):
        """
        Determines the loss of the model when run on inputs X with ground truths y.

        Args:
            X (numpy.ndarray): Batch of model inputs
            y (numpy.ndarray): Batch of ground truths per model inputs

        Raises:
            NotImplementedError: Raised if this function is not overridden by subclasses.

        Returns:
            numpy.float32: loss of the function on the current inputs
        """
        raise NotImplementedError

    @abc.abstractmethod
    def grad(self):
        """
        Returns the gradients of the model parameters after the previous call to loss(),
        in the same order as parameters()

        Raises:
            NotImplementedError: Raised if this function is not overriden by subclasses.

        Returns:
            Tuple: set of gradients for all model parameters
        """
        raise NotImplementedError
