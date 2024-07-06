# Quadrature Points Mapping in 2D and 3D + Legendre polynomials in 1D
THIS REPOSITORY IS FOR LEARNING THE DG SCHEME.

This repository contains Python scripts to generate and visualize Gauss and Gauss-Lobatto quadrature points in 2D and 3D. Quadrature points are used in numerical integration to approximate the integral of functions.
Comparison of the quadrature points in 2D can be done with comparison_of_quad_points_in2d.py. You'll get the following image.
<!-- ![image](figures/Gauss_Lobbato_comparison2d.png | width = 100) -->
<img src="https://github.com/Sho-Bob/DG-learner/blob/main/figures/Gauss_Lobbato_comparison2d.png" width ="500">
In addition, you can compare those quadrature points in 3D with comparison_of_quadrature_points.py. You'll get the following image.
<!-- ![3d comparison](figures/3d.png | width = 100) -->
<img src="https://github.com/Sho-Bob/DG-learner/blob/main/figures/3d.png" width ="500">
In this repository, you can find some codes to describe lagrange polynomials defined on [-1,1].
<!-- ![image](figures/legendre_poly.png | width = 100) -->
<img src="https://github.com/Sho-Bob/DG-learner/blob/main/figures/legendre_poly.png" width ="500">

In the DG scheme, we map an element in a physical plane to the reference plane with the Lagrange polynomial basis. The following equation is used to map the geometry vertices to the reference plane.
$x(\xi, \eta), y(\xi, \eta) = \sum_{i=1}^{n} \ell_i(\xi, \eta) (x_i, y_i)$
Here, $\ell_i(\xi, \eta) = \left(\prod_{\substack{j \neq i}} \frac{\xi - \xi_j}{\xi_i - \xi_j}\right) \left(\prod_{\substack{j \neq i}} \frac{\eta - \eta_j}{\eta_i - \eta_j}\right)$.
$\ell_i(\xi, \eta) (x_i, y_i)$ is $(x_i, y_i)$ at $(\xi_i, \eta_i)$ which is corresponds to $(x_i, y_i)$ in a physical coordinates.
The code is 'mapping.py', and this will give you the following result.
<img src="https://github.com/Sho-Bob/DG-learner/blob/main/figures/mapping.png" width ="500">

## Point
In some papers, you'll find $[x_{i-1/2}, x_{i+1/2}] \times [y_{i-1/2}, y_{i+1/2}]$ is defined with both Gauss quadrature points and Gauss-Lobatto quadrature points. To visualize this crazy domain, this repositpry includes 'gauss_gausslobatto.py'. The grid points in the target domain is like this. $S_x$ denotes x-coordinates defined with the Gauss points, $\hat{S_y}$ denotes y-coordinates defined with the Gauss-Lobatto points. 
<!-- ![image](figures/crazy.png | width = 100) -->
<img src="https://github.com/Sho-Bob/DG-learner/blob/main/figures/crazy.png" width ="500">

## Introduction
The scripts in this repository provide functions to calculate Gauss and Gauss-Lobatto quadrature points and weights. Additionally, the scripts include visualization tools to plot these points in both 2D and 3D spaces.

## Requirements
- Python 3.x
- NumPy
- Matplotlib

## Reference
For Japanese learners, [this website](https://slpr.sakura.ne.jp/sikinote/docs/numeric/integration/gauss-quadrature/#mjx-eqn-e3) is very good.

You can run those code with:
```sh
python *.py
