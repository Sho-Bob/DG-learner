import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss

def lobatto_points_and_weights(n):
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

    w = 2 / (n * (n - 1) * P[:, n - 1]**2)
    return x, w

def gauss_lobatto_quadrature_2d(n):
    points_1d, weights_1d = lobatto_points_and_weights(n)
    points_2d = np.array([[x, y] for x in points_1d for y in points_1d])
    weights_2d = np.array([wx * wy for wx in weights_1d for wy in weights_1d])
    return points_2d, weights_2d

def gauss_quadrature_2d(n):
    points_1d, weights_1d = leggauss(n)
    points_2d = np.array([[x, y] for x in points_1d for y in points_1d])
    weights_2d = np.array([wx * wy for wx in weights_1d for wy in weights_1d])
    return points_2d, weights_2d

# Number of quadrature points in one dimension
n = 5  

# Generate Gauss-Lobatto and Gauss quadrature points and weights
lobatto_points, lobatto_weights = gauss_lobatto_quadrature_2d(n)
gauss_points, gauss_weights = gauss_quadrature_2d(n)

# Plot the 2D Gauss-Lobatto and Gauss quadrature points
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(gauss_points[:,0], gauss_points[:,1], c='r', marker='o', s=100, label='Gauss')
ax.scatter(lobatto_points[:,0], lobatto_points[:,1], c='b', marker='^', s=100, label='Gauss-Lobatto')

ax.set_xlabel('X', fontsize=14)
ax.set_ylabel('Y', fontsize=14)
ax.set_title('2D Gauss-Lobatto and Gauss Quadrature Points', fontsize=16)
ax.legend()

# Add grid for better visualization
ax.grid(True)

plt.show()