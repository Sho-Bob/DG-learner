import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lobatto_points_and_weights(n):
    """
    Generates Gauss-Lobatto quadrature points and weights for a given number of points n.

    Parameters:
    n (int): Number of quadrature points in one dimension.

    Returns:
    tuple: A tuple containing the quadrature points and weights.
    """
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

def gauss_lobatto_quadrature_3d(n):
    """
    Generates Gauss-Lobatto quadrature points and weights in three dimensions.

    Parameters:
    n (int): Number of quadrature points in one dimension.

    Returns:
    tuple: A tuple containing the quadrature points and weights for 3D integration.
           - points (ndarray): An array of shape (n**3, 3) containing the quadrature points.
           - weights (ndarray): An array of shape (n**3,) containing the corresponding weights.
    """
    points_1d, weights_1d = lobatto_points_and_weights(n)
    
    points_3d = np.array([[x, y, z] for x in points_1d for y in points_1d for z in points_1d])
    weights_3d = np.array([wx * wy * wz for wx in weights_1d for wy in weights_1d for wz in weights_1d])
    
    return points_3d, weights_3d

# Example usage
n = 5  # Number of quadrature points in one dimension
points, weights = gauss_lobatto_quadrature_3d(n)

# Plot the 3D Gauss-Lobatto quadrature points
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:,1], points[:,2], c='r', marker='o', s=100)

ax.set_xlabel('X', fontsize=14)
ax.set_ylabel('Y', fontsize=14)
ax.set_zlabel('Z', fontsize=14)
ax.set_title('3D Gauss-Lobatto Quadrature Points', fontsize=16)

# Add grid for better visualization
ax.grid(True)

# Adjust the viewpoint for better clarity
ax.view_init(elev=20., azim=30)

plt.show()