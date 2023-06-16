import numpy as np

def schwefel_function(solution):
    dimension = len(solution)
    sum_term = 0.0
    product_term = 1.0

    for i in range(dimension):
        sum_term += solution[i]
        product_term *= np.sin(np.sqrt(np.abs(solution[i])))

    fitness = 418.9829 * dimension - sum_term + product_term

    return fitness


def rastrigin_function(solution):
    dimension = len(solution)
    a = 10.0

    fitness = a * dimension
    for i in range(dimension):
        fitness += (solution[i] ** 2) - (a * np.cos(2 * np.pi * solution[i]))

    return fitness


def rosenbrock_function(solution):
    dimension = len(solution)
    fitness = 0

    for i in range(dimension - 1):
        fitness += 100 * (solution[i+1] - solution[i]**2)**2 + (solution[i] - 1)**2

    return fitness


