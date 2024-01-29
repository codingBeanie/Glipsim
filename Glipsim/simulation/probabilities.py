import numpy as np
import random

# L: maximum value of the function
# k: steepness of the function
#   k > 0: steepness increases
#   k < 0: steepness decreases
# h: point in which the function is 0.5


def probability_reproduction(age, L=1, k=-0.25, h=38):
    return L / (1 + np.exp(-k * (age - h)))


def probability_surviving(age, L=1, k=-0.2, h=85):
    return (L / (1 + np.exp(-k * (age - h))))


def logistic_function(value, steepness, halved, maximum=10):
    return maximum / (1 + np.exp(steepness * (value - halved)))


def evaluation_reproduction(age, maximum=10, steepness=2, halved=10):
    return maximum / (1 + np.exp(steepness * (age - halved)))
