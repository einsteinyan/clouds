import numpy as np

def get_integral_approximation(f, a, b):
    """Creates a master

    Args:
        f (fn): function to be evaluated.
        a (float): lower bound.
        b (float): upper bound.

    Returns:
        y (float): numerical approximenation of the given function
    """
    return (b-a)*np.mean(f)