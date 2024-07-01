import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# 範囲 [-1, 1] で等間隔に5点
x_points = np.linspace(-1, 1, 5)
y_points = np.random.rand(5)  

# レジェンドル多項式の計算
def legendre_basis(x, degree):
    """
    レジェンドル多項式を計算
    x: 計算する点の配列
    degree: レジェンドル多項式の次数
    """
    P = legendre(degree)
    return P(x)

# 細かいx軸データでプロット
x_fine = np.linspace(-1.1, 1.1, 400)
plt.figure(figsize=(10, 6))

# 各レジェンドル多項式をプロット
for j in range(len(x_points)):
    Pj = legendre_basis(x_fine, j)
    plt.plot(x_fine, Pj, label=f'$P_{{ {j} }}(x)$')

# 元のデータ点をプロット
plt.scatter(x_points, y_points, color='red', s=100, zorder=5, label='Data Points')

# プロット設定
plt.title('Legendre Polynomials')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()