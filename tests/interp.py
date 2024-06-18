import numpy as np
from scipy.interpolate import interp1d

# 假设 func1_x 和 func1_y 是第一个函数的自变量和因变量
# 假设 func2_x 和 func2_y 是第二个函数的自变量和因变量
func1_x = np.array([1, 2, 3, 5])
func1_y = np.array([1, 4, 9, 16])

func2_x = np.array([1, 2, 3, 4, 6])
func2_y = np.array([5, 6, 7, 8, 10])

# 创建插值函数
interp_func1 = interp1d(func1_x, func1_y, kind='cubic', fill_value="extrapolate")
interp_func2 = interp1d(func2_x, func2_y, kind='cubic', fill_value="extrapolate")

# 确定公共的自变量集合，这里我们取两个函数自变量的并集
common_x = np.union1d(func1_x, func2_x)

# 在公共的自变量集合上执行插值
interp_values1 = interp_func1(common_x)
interp_values2 = interp_func2(common_x)

# 逐点相乘
product_values = interp_values1 * interp_values2

print(product_values)