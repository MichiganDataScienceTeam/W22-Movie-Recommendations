import abc
import numpy


class Recommender(abc.ABC):
    """
    An abstract base class for a recommender algorithm
    """

    @abc.abstractmethod
    def train(utility_matrix: numpy.ndarray):
        """
        Trains the recommender on the sparse (incomplete) utility matrix to
        prepare for predictions. This function will be called once after instantiation,
        and no further calls will be made.

        Args:
            utility_matrix (numpy.ndarray): The input utility matrix.

        Raises:
            NotImplementedError: Raised if this function is not overwritten by subclasses.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def predict(user_ratings: numpy.ndarray) -> numpy.ndarray:
        """
        Predicts the expected ratings given a sparse input vector.

        Args:
            user_ratings (numpy.ndarray): Input ratings. Will be sparse (not all ratings will be given).

        Raises:
            NotImplementedError: Raised if this function is not overwritten by subclasses.

        Returns:
            numpy.ndarray: Predicted ratings for this user.
        """
        raise NotImplementedError
