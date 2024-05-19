# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
desired_time_steps = [0, 10, 50, 100]

# Create a 100x100 grid initialized to zero
population = np.zeros((100, 100))

# Randomly pick an outbreak starting point
outbreak = np.random.choice(range(100), 2)
# Initialize the outbreak point as infected
population[outbreak[0], outbreak[1]] = 1

# Simulate the process for 100 time steps
for t in range(100): 
    # Find infected points
    infectedIndex = np.where(population == 1)

    # Loop through all infected points
    for index in range(len(infectedIndex[0])): 
        x = infectedIndex[0][index]
        y = infectedIndex[1][index]
        # Infect each neighbour with probability beta
        for xNeighbour in range(x-1, x+2):
            for yNeighbour in range(y-1, y+2):
                # Don't infect yourself!
                if (xNeighbour, yNeighbour) != (x, y):
                    # Make sure don't fall off an edge
                    if 0 <= xNeighbour < 100 and 0 <= yNeighbour < 100:
                        # Only infect neighbours that are not already infected!
                        if population[xNeighbour, yNeighbour] == 0:
                            population[xNeighbour, yNeighbour] = np.random.choice([0, 1], p=[1-beta, beta])
        # Infected becomes recovered
        if np.random.rand() < gamma:
            population[x, y] = 2

    if t in desired_time_steps:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.title(f'Time Step {t}')
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.colorbar()
        plt.show()
        plt.clf()
