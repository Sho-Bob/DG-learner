import numpy as np
import matplotlib.pyplot as plt

# 範囲 [-1, 1] で等間隔に5点
x_points = np.linspace(-1, 1, 5)
y_points = np.random.rand(5)  # ここではランダムな値を生成していますが、任意の値に設定可能です

# ラグランジュ基底多項式の計算
def lagrange_basis(x, x_points, j):
    """
    ラグランジュ基底多項式を計算
    x: 計算する点の配列
    x_points: すべてのサポートポイント
    j: 対象とするサポートポイントのインデックス
    """
    term = np.ones_like(x)
    for i in range(len(x_points)):
        if i != j:
            term *= (x - x_points[i]) / (x_points[j] - x_points[i])
    return term

# 細かいx軸データでプロット
x_fine = np.linspace(-1.1, 1.1, 400)
plt.figure(figsize=(10, 6))

# ラグランジュ補間多項式全体の計算
L = np.zeros_like(x_fine)
for j in range(len(x_points)):
    L += y_points[j] * lagrange_basis(x_fine, x_points, j)

# 各基底多項式をプロット
for j in range(len(x_points)):
    phi = lagrange_basis(x_fine, x_points, j)
    plt.plot(x_fine, phi, label=f'$\phi_{{ {j+1} }}(x)$')

# ラグランジュ補間多項式をプロット
plt.plot(x_fine, L, 'k-', linewidth=2, label='Lagrange Interpolating Polynomial')

# 元のデータ点をプロット
plt.scatter(x_points, y_points, color='red', s=100, zorder=5, label='Data Points')

# プロット設定
plt.title('Lagrange Polynomial Interpolation with 5 Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()