import numpy as np
from scipy.interpolate import BarycentricInterpolator
from scipy.integrate import quad

# 節点の設定
x_points = np.linspace(-1, 1, 5)
y_values = np.zeros(5)
y_values[2] = 1  # L_2(x) を中心点 x=0 で 1 に設定

# ラグランジュ補間
interpolator = BarycentricInterpolator(x_points, y_values)
L_2 = lambda x: interpolator(x)

# 積分
integral, error = quad(L_2, -1, 1)
print(f"Integral of L_2(x) over [-1, 1] is approximately {integral:.6f}, with error estimate {error:.6e}")