import numpy as np
import matplotlib.pyplot as plt

# 设置时间向量
t = np.linspace(-10, 10, 2000)
delta_t = t[1] - t[0]

# 设置时域信号x(t)
x_t = np.exp(-t**2)

# 进行傅里叶变换并调整尺度
X_jw = np.fft.fft(x_t)
X_jw_shifted = np.fft.fftshift(X_jw) * delta_t

# 设置频率向量
omega = np.fft.fftfreq(len(t), d=delta_t) * 2 * np.pi
omega = np.fft.fftshift(omega)

# 画图
plt.figure(figsize=(12, 8))

# 时域信号
plt.subplot(2, 1, 1)
plt.plot(t, x_t)
plt.title('Time Domain Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim([-10, 10])  # 设置x轴的显示范围为[-10, 10]

# 频域信号
plt.subplot(2, 1, 2)
plt.plot(omega, np.abs(X_jw_shifted))
plt.title('Frequency Domain Signal X(jω)')
plt.xlabel('Frequency (ω)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.tight_layout()

# 保存图片
plt.savefig('fft.png')
plt.close()
