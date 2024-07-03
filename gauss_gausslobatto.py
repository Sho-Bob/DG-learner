import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss

def compute_gauss_lobatto_points(n):
    x = np.cos(np.linspace(0, np.pi, n))
    P = np.zeros((n, n))
    xold = 2
    while np.max(np.abs(x - xold)) > np.finfo(float).eps:
        xold = np.copy(x)
        P[:, 0] = 1
        P[:, 1] = x
        for k in range(2, n):
            P[:, k] = ((2 * k - 1) * x * P[:, k - 1] - (k - 1) * P[:, k - 2]) / k
        x = xold - (x * P[:, n - 1] - P[:, n - 2]) / (n * P[:, n - 1])
    return x

def create_grid_points():
    n_gauss = 5
    n_gauss_lobatto = 6

    # Gauss quadrature points
    gauss_points, _ = leggauss(n_gauss)
    
    # Gauss-Lobatto quadrature points
    gauss_lobatto_points = compute_gauss_lobatto_points(n_gauss_lobatto)

    # Create S_i^x x Ŝ_j^y and Ŝ_i^x x S_j^y sets
    S1_x = np.tile(gauss_points, n_gauss_lobatto)
    S1_y = np.repeat(gauss_lobatto_points, n_gauss)
    S2_x = np.tile(gauss_lobatto_points, n_gauss)
    S2_y = np.repeat(gauss_points, n_gauss_lobatto)

    return S1_x, S1_y, S2_x, S2_y

def visualize_S_K():
    S1_x, S1_y, S2_x, S2_y = create_grid_points()

    plt.figure(figsize=(10, 8))
    
    plt.scatter(S1_x, S1_y, color='blue', marker='^', label='$S_i^x \\times \\hat{S}_j^y$')
    plt.scatter(S2_x, S2_y, color='red', marker='o', label='$\\hat{S}_i^x \\times S_j^y$')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Visualization of $S_K$ with Gauss and Gauss-Lobatto Points')
    plt.legend()
    plt.grid(True)
    plt.show()

visualize_S_K()