# -*- coding: utf-8 -*-
"""Random Walking

Computational Physics by Rubin H. Landau - Third edition
Pag. 77: 4.3.2 Implementation: Random Walk

Bruno O. and Enzo G.
"""

import numpy as np
import matplotlib.pyplot as plt

# Number of steps in the random walk
N = 1000

# Starting point
x, y = 0, 0

# List to store the positions
positions = [(x, y)]

# Perform the random walk
for _ in range(N):
    # Random step in [-1, 1] range for both x and y
    delta_x_prime = np.random.uniform(-1, 1)
    delta_y_prime = np.random.uniform(-1, 1)

    # Calculate the length of the step
    length = np.sqrt(delta_x_prime**2 + delta_y_prime**2)

    # Normalize to unit length
    delta_x = delta_x_prime / length
    delta_y = delta_y_prime / length

    # Update position
    x += delta_x
    y += delta_y

    # Store the new position
    positions.append((x, y))

# Extract the x and y positions for plotting
x_positions, y_positions = zip(*positions)

# Plot the random walk
plt.figure(figsize=(8, 8))
plt.plot(x_positions, y_positions, label='Random Walk')
plt.scatter(x_positions[-1], y_positions[-1], color='red', label='Final Position')
plt.scatter(x_positions[0], y_positions[0], color='yellow', label='Initial Position')
plt.title(f"2D Random Walk with {N} Steps")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend()
plt.axis('equal')
plt.show()

# Compute the final displacement from the origin
final_displacement = np.sqrt(x**2 + y**2)
print(f"Final displacement: {final_displacement}")

import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Função para caminhada aleatória em 2D
def random_walk_2d(steps):
    x, y = 0, 0
    positions = [(x, y)]
    for N in range(steps):
        delta_x_prime = random.uniform(-1, 1)
        delta_y_prime = random.uniform(-1, 1)

        L = math.sqrt(delta_x_prime**2 + delta_y_prime**2)
        delta_x = delta_x_prime / L
        delta_y = delta_y_prime / L

        x += delta_x
        y += delta_y

        # Lista das novas posições
        positions.append((x, y))

    return x, y

# Extract the x and y positions for plotting
x_positions, y_positions = zip(*positions)

# Plot the random walk
plt.figure(figsize=(8, 8))
plt.plot(x_positions, y_positions, label='Random Walk')
plt.scatter(x_positions[-1], y_positions[-1], color='red', label='Posição final')
plt.scatter(x_positions[0], y_positions[0], color='yellow', label='Posição inicial')
plt.title(f"2D Random Walk com {N} Passos")
plt.xlabel("Posição em X")
plt.ylabel("Posição em Y")
plt.legend()
plt.axis('equal')
plt.show()

# Compute the final displacement from the origin
final_displacement = np.sqrt(x**2 + y**2)
print(f"Deslocamento total: {final_displacement}")

# Função para verificar as correlações (assunções teóricas)
def check_assumptions(N, K, dim, x_positions, y_positions):
    x_correlation = []
    x_positions = list(x_positions)
    y_positions = list(y_positions)

    for _ in range(K):
        if dim == 2:
            # Caminhada 2D
            delta_x = np.diff(x_positions)
            delta_y = np.diff(y_positions)
        else:
          print('Não construído')

        x_correlation.append(np.corrcoef(delta_x, delta_y)[0, 1])  # Correlação entre os passos em x e y

    print(f"Correlações médias (x, y) para caminhada {dim}D: {np.mean(x_correlation)}")
    print(f"Correlação entre os passos em x (x, x) para caminhada {dim}D: {np.corrcoef(delta_x, delta_x)[0, 1]}")

# Função para caminhada aleatória em 3D
def random_walk_3d(steps):
    x, y, z = 0, 0, 0
    for _ in range(steps):
        delta_x_prime = random.uniform(-1, 1)
        delta_y_prime = random.uniform(-1, 1)
        delta_z_prime = random.uniform(-1, 1)

        L = math.sqrt(delta_x_prime**2 + delta_y_prime**2 + delta_z_prime**2)
        delta_x = delta_x_prime / L
        delta_y = delta_y_prime / L
        delta_z = delta_z_prime / L

        x += delta_x
        y += delta_y
        z += delta_z

    return x, y, z

# Função para calcular a distância quadrada (R^2)
def squared_distance(x, y, z=None):
    if z is None:
        return x**2 + y**2
    else:
        return x**2 + y**2 + z**2

# Função para rodar múltiplos experimentos e calcular a média do quadrado da distância
def run_trials(N, K, dim):
    R_squared_values = []

    for _ in range(K):
        # Para caminhada em 2D
        if dim == 2:
            final_x, final_y = random_walk_2d(N)
            R_squared = squared_distance(final_x, final_y)

        # Para caminhada em 3D
        elif dim == 3:
            final_x, final_y, final_z = random_walk_3d(N)
            R_squared = squared_distance(final_x, final_y, final_z)

        R_squared_values.append(R_squared)

    mean_R_squared = np.mean(R_squared_values)
    return mean_R_squared

# Função para plotar a distância RMS vs sqrt(N)
def plot_RMS_vs_sqrtN(max_steps, max_trials, dim):
    step_sizes = range(10, max_steps + 1, 10)  # Passos de 10 até 1000
    RMS_values = []

    for N in step_sizes:
        K = int(math.sqrt(N))  # Aproximadamente K ≈ sqrt(N)
        mean_R_squared = run_trials(N, K, dim)
        RMS_values.append(math.sqrt(mean_R_squared))

    plt.figure(figsize=(8, 6))
    plt.plot([math.sqrt(N) for N in step_sizes], RMS_values, marker='o', label=f'{dim}D Random Walk')
    plt.xlabel('N')
    plt.ylabel('RMS')
    plt.title(f'{dim}D Random Walk: RMS vs N')
    plt.grid(True)
    plt.legend()
    plt.show()

# Análise da caminhada aleatória 2D
plot_RMS_vs_sqrtN(1000, 32, 2)

# Verificação das suposições para caminhada 2D
check_assumptions(1000, 32, 2, x_positions, y_positions)

# Análise da caminhada aleatória 3D
plot_RMS_vs_sqrtN(1000, 32, 3)

import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Função para caminhada aleatória em 2D
def random_walk_2d(steps):
    x, y = 0, 0
    for _ in range(steps):
        delta_x_prime = random.uniform(-1, 1)
        delta_y_prime = random.uniform(-1, 1)

        L = math.sqrt(delta_x_prime**2 + delta_y_prime**2)
        delta_x = delta_x_prime / L
        delta_y = delta_y_prime / L

        x += delta_x
        y += delta_y

    return x, y

# Função para caminhada aleatória em 3D
def random_walk_3d(steps):
    x, y, z = 0, 0, 0
    for _ in range(steps):
        delta_x_prime = random.uniform(-1, 1)
        delta_y_prime = random.uniform(-1, 1)
        delta_z_prime = random.uniform(-1, 1)

        L = math.sqrt(delta_x_prime**2 + delta_y_prime**2 + delta_z_prime**2)
        delta_x = delta_x_prime / L
        delta_y = delta_y_prime / L
        delta_z = delta_z_prime / L

        x += delta_x
        y += delta_y
        z += delta_z

    return x, y, z

# Função para calcular a distância quadrada (R^2)
def squared_distance(x, y, z=None):
    if z is None:
        return x**2 + y**2
    else:
        return x**2 + y**2 + z**2

# Função para rodar múltiplos experimentos e calcular a média do quadrado da distância
def run_trials(N, K, dim=2):
    R_squared_values = []

    for _ in range(K):
        # Para caminhada em 2D
        if dim == 2:
            final_x, final_y = random_walk_2d(N)
            R_squared = squared_distance(final_x, final_y)

        # Para caminhada em 3D
        elif dim == 3:
            final_x, final_y, final_z = random_walk_3d(N)
            R_squared = squared_distance(final_x, final_y, final_z)

        R_squared_values.append(R_squared)

    mean_R_squared = np.mean(R_squared_values)
    return mean_R_squared

# Função para verificar as correlações (assunções teóricas)
def check_assumptions(N, K, dim=2):
    x_correlation = []
    y_correlation = []

    for _ in range(K):
        if dim == 2:
            # Caminhada 2D
            x_positions, y_positions = random_walk_2d(N)
            delta_x = np.diff(x_positions)
            delta_y = np.diff(y_positions)

        elif dim == 3:
            # Caminhada 3D
            x_positions, y_positions, z_positions = random_walk_3d(N)
            delta_x = np.diff(x_positions)
            delta_y = np.diff(y_positions)
            delta_z = np.diff(z_positions)

        x_correlation.append(np.corrcoef(delta_x, delta_y)[0, 1])  # Correlação entre os passos em x e y

    print(f"Correlações médias (x, y) para caminhada {dim}D: {np.mean(x_correlation)}")
    print(f"Correlação entre os passos em x (x, x) para caminhada {dim}D: {np.corrcoef(delta_x, delta_x)[0, 1]}")

# Função para plotar a distância RMS vs sqrt(N)
def plot_RMS_vs_sqrtN(max_steps=1000, max_trials=32, dim=2):
    step_sizes = range(10, max_steps + 1, 10)  # Passos de 10 até 1000
    RMS_values = []

    for N in step_sizes:
        K = int(math.sqrt(N))  # Aproximadamente K ≈ sqrt(N)
        mean_R_squared = run_trials(N, K, dim)
        RMS_values.append(math.sqrt(mean_R_squared))

    plt.figure(figsize=(8, 6))
    plt.plot([math.sqrt(N) for N in step_sizes], RMS_values, marker='o', label=f'{dim}D Random Walk')
    plt.xlabel(r'$\sqrt{N}$')
    plt.ylabel(r'$R_{\text{rms}}$')
    plt.title(f'{dim}D Random Walk: RMS Distance vs $\sqrt{N}$')
    plt.grid(True)
    plt.legend()
    plt.show()

# Análise da caminhada aleatória 2D
plot_RMS_vs_sqrtN(dim=2)

# Verificação das suposições para caminhada 2D
check_assumptions(1000, 32, dim=2)

# Análise da caminhada aleatória 3D
plot_RMS_vs_sqrtN(dim=3)

# Verificação das suposições para caminhada 3D
check_assumptions(1000, 32, dim=3)