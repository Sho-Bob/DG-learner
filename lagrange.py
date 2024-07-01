# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
# 与えられたxの値
x_points = np.array([1, 2, 3, 4, 5])

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
x_fine = np.linspace(0.5, 5.5, 400)
plt.figure(figsize=(10, 6))
# %%
# 各基底多項式をプロット
for j in range(len(x_points)):
    phi = lagrange_basis(x_fine, x_points, j)
    plt.plot(x_fine, phi, label=f'$\phi_{j+1}(x)$')

# プロット設定
plt.title('Lagrange Basis Polynomials')
plt.xlabel('x')
plt.ylabel('$\phi_j(x)$')
plt.legend()
plt.grid(True)
plt.show()