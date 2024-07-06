import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Lagrange basis functions for the unit square
def L1(xi, eta):
    return (1 - xi) * (1 - eta)

def L2(xi, eta):
    return xi * (1 - eta)

def L3(xi, eta):
    return xi * eta

def L4(xi, eta):
    return (1 - xi) * eta

# Define the physical coordinates of the quadrilateral's vertices in 3D
vertices = np.array([[1, 2, 1], [4, 2, 2], [4, 5, 3], [1, 5, 4]])

# Mapping function using the Lagrange basis functions
def map_to_physical(xi, eta, vertices):
    return (L1(xi, eta) * vertices[0] +
            L2(xi, eta) * vertices[1] +
            L3(xi, eta) * vertices[2] +
            L4(xi, eta) * vertices[3])

# Generate a grid of points in the reference plane
xi_values = np.linspace(0, 1, 20)
eta_values = np.linspace(0, 1, 20)
xi_grid, eta_grid = np.meshgrid(xi_values, eta_values)

# Map the grid points to the physical plane
x_mapped = np.zeros_like(xi_grid)
y_mapped = np.zeros_like(eta_grid)
z_mapped = np.zeros_like(xi_grid)
for i in range(xi_grid.shape[0]):
    for j in range(xi_grid.shape[1]):
        xi = xi_grid[i, j]
        eta = eta_grid[i, j]
        mapped_point = map_to_physical(xi, eta, vertices)
        x_mapped[i, j] = mapped_point[0]
        y_mapped[i, j] = mapped_point[1]
        z_mapped[i, j] = mapped_point[2]

# Define a specific point in the reference plane
xi_point = 0.3
eta_point = 0.4
mapped_point = map_to_physical(xi_point, eta_point, vertices)

# Plot the mapped 3D surface
fig = plt.figure(figsize=(12, 8))

# Plot the reference plane
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(xi_grid, eta_grid, np.zeros_like(xi_grid), cmap='viridis', edgecolor='k', alpha=0.6)
ax1.scatter(xi_point, eta_point, 0, c='red', marker='o', s=100)  # Add corresponding red point
ax1.set_title('Reference Plane')
ax1.set_xlabel('xi')
ax1.set_ylabel('eta')
ax1.set_zlabel('z')
ax1.axis('equal')

# Plot the physical plane
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x_mapped, y_mapped, z_mapped, cmap='viridis', edgecolor='k', alpha=0.6)
ax2.scatter(mapped_point[0], mapped_point[1], mapped_point[2], c='red', marker='o', s=100)  # Add corresponding red point

# Plot the vertices of the physical plane
ax2.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='black', s=100, label='Vertices')
for i in range(vertices.shape[0]):
    ax2.text(vertices[i, 0], vertices[i, 1], vertices[i, 2], f'V{i}', color='black')

ax2.set_title('Physical Plane')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.legend()

plt.tight_layout()
plt.show()