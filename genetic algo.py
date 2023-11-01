import random

# Genetic Algorithm Parameters
population_size = 100
num_generations = 100
mutation_rate = 0.1

# Define the fitness function (replace with your problem-specific function)
def fitness(solution):
    return solution

# Initialize a population with random solutions
def initialize_population(size):
    return [random.uniform(0, 10) for _ in range(size)]

# Perform mutation with a certain probability
def mutate(solution):
    if random.random() < mutation_rate:
        return solution + random.uniform(-1, 1)
    return solution

# Main Genetic Algorithm
population = initialize_population(population_size)
for generation in range(num_generations):
    new_population = []
    for _ in range(population_size):
        parent = random.choice(population)
        child = mutate(parent)
        new_population.append(child)

    population = new_population

# Get the best solution from the final population
best_solution = max(population, key=fitness)

print("Best solution:", best_solution)
print("Best fitness:", fitness(best_solution))
