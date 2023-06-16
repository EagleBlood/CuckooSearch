import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

def levy_flight(step_length, lambda_value):
    numerator = lambda_value * gamma(lambda_value) * math.sin(math.pi * lambda_value / 2)
    denominator = math.pi * ((step_length ** (1 + lambda_value)) * gamma(1 + lambda_value) * lambda_value ** 2)
    return numerator / denominator

def levy_flight_plot(step_length, lambda_value, num_steps):
    x = [0]
    y = [0]

    for _ in range(num_steps):
        U = random.normalvariate(0, 1)
        V = random.normalvariate(0, 1)
        s = (U / abs(V)) ** (1 / lambda_value)
        theta = 2 * math.pi * V

        dx = step_length * s * math.sin(theta)
        dy = step_length * s * math.cos(theta)

        x.append(x[-1] + dx)
        y.append(y[-1] + dy)

    # Wykres z połączonymi kreskami
    plt.plot(x, y, linestyle='-', marker='', color='blue')

    # Ustawienia osi
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Wykres lotów Levy'ego")

    # Wyświetlenie wykresu
    plt.show()

def generate_initial_solution():
    # Tutaj zaimplementuj losową generację początkowego rozwiązania
    return [random.uniform(0, 1) for _ in range(10)]

def evaluate_solution(solution):
    # Tutaj zaimplementuj obliczanie wartości funkcji kryterialnej dla danego rozwiązania
    fitness = sum(solution)  # Przykładowe obliczenie wartości funkcji kryterialnej
    return fitness

def cuckoo_search_algorithm(population_size, max_iterations):
    nests = [generate_initial_solution() for _ in range(population_size)]
    best_solution = nests[0]
    
    for iteration in range(max_iterations):
        for i in range(population_size):
            current_solution = nests[i]
            
            # Generowanie nowego rozwiązania za pomocą lotu Lévy'ego
            step_length = levy_flight(1, 1.5)  # Przykładowe wartości lambda_value = 1.5
            new_solution = [current_solution[j] + step_length * random.uniform(-1, 1) for j in range(len(current_solution))]
            
            # Ocena nowego rozwiązania
            current_fitness = evaluate_solution(current_solution)
            new_fitness = evaluate_solution(new_solution)
            
            # Aktualizacja gniazda, jeśli nowe rozwiązanie jest lepsze
            if new_fitness < current_fitness:
                nests[i] = new_solution
                
            # Porzucanie części gorszych rozwiązań i ich zastąpienie nowymi
            discard_probability = 0.25  # Przykładowe prawdopodobieństwo porzucenia
            if random.random() < discard_probability:
                nests[i] = generate_initial_solution()
        
        # Sortowanie gniazd względem wartości funkcji kryterialnej
        nests.sort(key=lambda x: evaluate_solution(x))
        
        # Aktualizacja najlepszego rozwiązania
        if evaluate_solution(nests[0]) < evaluate_solution(best_solution):
            best_solution = nests[0]
    
    return best_solution

# Wywołanie algorytmu kukułczego
population_size = 10
max_iterations = 100
best_solution = cuckoo_search_algorithm(population_size, max_iterations)

print("Najlepsze znalezione rozwiązanie:", best_solution)

# Wywołanie funkcji do rysowania lotu Lévy'ego
step_length = 1
lambda_value = 1.5
num_steps = 1000

levy_flight_plot(step_length, lambda_value, num_steps)
