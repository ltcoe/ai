import random

# Define the objective function to be maximized (you can replace this with your own function)
def objective_function(x):
    return -x**2  # Negative of a simple quadratic function (to maximize)

# Hill climbing algorithm
def hill_climbing(max_iterations, step_size, initial_solution):
    current_solution = initial_solution
    for iteration in range(max_iterations):
        neighbors = [current_solution + step_size, current_solution - step_size]
        neighbor_values = [objective_function(neighbor) for neighbor in neighbors]
        best_neighbor_value = max(neighbor_values)  # Maximization

        if best_neighbor_value > objective_function(current_solution):
            current_solution = neighbors[neighbor_values.index(best_neighbor_value)]
        else:
            break

    return current_solution

# Main
if __name__ == "__main__":
    max_iterations = 100
    step_size = 0.1
    initial_solution = random.uniform(-10, 10)  # Random initial solution in the range [-10, 10]

    best_solution = hill_climbing(max_iterations, step_size, initial_solution)
    best_value = objective_function(best_solution)

    print("Best solution:", best_solution)
    print("Best value:", best_value)
