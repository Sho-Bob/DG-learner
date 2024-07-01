import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_jacobi

def radau_polynomial(n, x):
    """
    Radau IIA 多項式を計算します。ここで、Jacobi 多項式 P^(1,0)_n を使用して、
    Radau 多項式を得るための変換を行います。
    """
    if n == 0:
        return np.ones_like(x)  # n=0 の場合、定数項 1
    else:
        return eval_jacobi(n - 1, 1, 0, x)

# -1 と 1 の間の点を生成
x = np.linspace(-1, 1, 400)

# 最大次数
max_degree = 5

# 図を初期化
plt.figure(figsize=(10, 6))

# 異なる次数の Radau 多項式をプロット
for n in range(max_degree + 1):
    y = radau_polynomial(n, x)
    plt.plot(x, y, label=f'n={n}')

plt.title('Radau IIA 多項式')
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.legend()
plt.grid(True)
plt.show()