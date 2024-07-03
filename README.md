# Quadrature Points Mapping in 2D and 3D + Legendre polynomials in 1D
THIS REPOSITORY IS FOR LEARNING THE DG SCHEME.

This repository contains Python scripts to generate and visualize Gauss and Gauss-Lobatto quadrature points in 2D and 3D. Quadrature points are used in numerical integration to approximate the integral of functions.
Comparison of the quadrature points in 2D can be done with comparison_of_quad_points_in2d.py. You'll get the following image.
<!-- ![image](figures/Gauss_Lobbato_comparison2d.png | width = 100) -->
<img src="https://github.com/Sho-Bob/DG-learner/blob/main/figures/Gauss_Lobbato_comparison2d.png" width ="100">
In addition, you can compare those quadrature points in 3D with comparison_of_quadrature_points.py. You'll get the following image.
![3d comparison](figures/3d.png | width = 100)

In this repository, you can find some codes to describe lagrange polynomials defined on [-1,1].
![image](figures/legendre_poly.png | width = 100)

## Point
In some papers, you'll find $[x_{i-frac{1}{2}}, x_{i+frac{1}{2}}] \times [x_{i-frac{1}{2}}, x_{i+frac{1}{2}}]$ is defined with both Gauss quadrature points and Gauss-Lobatto quadrature points. To visualize this crazy domain, this repositpry includes "gauss_gausslobatto.py". The grid points in the target domain is like this. $S_x$ denotes x-coordinates defined with the Gauss points, $\hat{S_y}$ denotes y-coordinates defined with the Gauss-Lobatto points. 
![image](figures/crazy.png | width = 100)

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
