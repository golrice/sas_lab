import numpy as np
import matplotlib.pyplot as plt

# 采样点数和频率范围
omega = np.linspace(-100, 100, 2000)
delta_omega = omega[1] - omega[0]

# 设置频域信号X(jω)
X_jw = 4 / (4 + omega**2)

# 进行移位处理
X_jw_shifted = np.fft.ifftshift(X_jw)

# 执行傅里叶逆变换并调整尺度
x_t = np.fft.ifft(X_jw_shifted) * len(omega) * delta_omega

x_t = np.real(x_t)  # 取实部，因为结果中可能含有虚部

# 设置时间向量
t = np.fft.fftfreq(len(omega), d=delta_omega/(2*np.pi))

# 确保时域信号在t=0处的值为1
x_t /= np.max(x_t)

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
plt.plot(omega, X_jw)
plt.title('Frequency Domain Signal X(jω)')
plt.xlabel('Frequency (ω)')
plt.ylabel('Magnitude')
plt.grid(True)


plt.tight_layout()

# 保存图片
plt.savefig('ifft.png')
plt.close()
