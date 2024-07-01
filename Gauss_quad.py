import numpy as np
from numpy.polynomial.legendre import leggauss
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gauss_quadrature_3d(n):
    """
    Generates Gauss quadrature points and weights in three dimensions.
    
    Parameters:
    n (int): Number of quadrature points in one dimension.
    
    Returns:
    tuple: A tuple containing the quadrature points and weights for 3D integration.
           - points (ndarray): An array of shape (n**3, 3) containing the quadrature points.
           - weights (ndarray): An array of shape (n**3,) containing the corresponding weights.
    """
    # Get the 1D Gauss-Legendre quadrature points and weights
    points_1d, weights_1d = leggauss(n)
    
    # Create the 3D grid of points and weights
    points_3d = np.array([[x, y, z] for x in points_1d for y in points_1d for z in points_1d])
    weights_3d = np.array([wx * wy * wz for wx in weights_1d for wy in weights_1d for wz in weights_1d])
    
    return points_3d, weights_3d

# Example usage
n = 7  # Number of quadrature points in one dimension
points, weights = gauss_quadrature_3d(n)

# Plot the 3D Gauss quadrature points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:,1], points[:,2], c='r', marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Gauss Quadrature Points')

plt.show()