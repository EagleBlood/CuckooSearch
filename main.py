import math
import matplotlib.pyplot as plt
import cuckoo as ck
import levy_flight as lf


# Wywołanie algorytmu kukułczego
population_size = 50  # Rozmiar populacji
max_iterations = 100  # Maksymalna ilosć iteracji
probability = 0.25    # prawdopodobieństwo
lower_bound = -10     # Dolna granica (Lb)
upper_bound = 10      # Górna granica (Ub)
best_solution = ck.cuckoo_search_algorithm(population_size, max_iterations, lower_bound, upper_bound, probability)
top_best_solution = best_solution[:5]


def plot(solution):
    x = [0]
    y = [0]

    for i in range(len(solution)):
        dx = solution[i] * math.sin(i)
        dy = solution[i] * math.cos(i)

        x.append(x[-1] + dx)
        y.append(y[-1] + dy)

    # Tworzenie pierwszego wykresu 'The Best Solution'
    plt.figure(2)
    plt.plot(x, y, linestyle='-', marker='', color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Wykres 'The Best Solution'")

    # Tworzenie drugiego wykresu 'Levy Flight'
    plt.figure(1)
    lf.levy_flight_plot(step_length, lambda_value, num_steps)

    # Wyświetlenie obu wykresów
    plt.show()


# Wywołanie funkcji do rysowania lotu Lévy'ego
step_length = 1
lambda_value = 1.5
num_steps = 1000

plot(top_best_solution)
