import numpy as np
import matplotlib.pyplot as plt
import os
import util

# constants
# eigenfunction 表示 频率响应
eigenfunction_path = os.path.join(os.path.dirname(__file__), "..", "resources", "eigenfunction.wav")
# vocal 表示 人声信息
vocal_path = os.path.join(os.path.dirname(__file__), "..", "resources", "vocal.wav")
# 保存时域和频域信号的图像
save_graph_path = os.path.join(os.path.dirname(__file__), "..", "resources", "graph.png")

# 保存经过LTI变换后的人声信号
save_vocal_path = os.path.join(os.path.dirname(__file__), "..", "resources", "vocal_after_transform.wav")

# 加载时域信号
eigenfunction_time_signal = util.TimeSignal.from_path(eigenfunction_path)
vocal_time_signal = util.TimeSignal.from_path(vocal_path)

# 转换成频域
eigenfunction_freq_signal = eigenfunction_time_signal.to_frequency()
vocal_freq_signal = vocal_time_signal.to_frequency()

# LTI transform
# 使用上面得到的eigenfunction和vocal的JW频谱，进行LTI变换
# S(jw) = eigenfunction_jw_shifted
# X(jw) = vocal_jw_shifted
# vocal_pure_jw = X(jw) * S(jw)
# 需要构造出 H(jw)

# plot graphs
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(eigenfunction_time_signal.time_axis, eigenfunction_time_signal.x_t)
plt.title("Eigenfunction")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(vocal_time_signal.time_axis, vocal_time_signal.x_t)
plt.title("Vocal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(eigenfunction_freq_signal.omega_axis, np.abs(eigenfunction_freq_signal.X_jw_shifted))
plt.title("Eigenfunction JW Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(vocal_freq_signal.omega_axis, np.abs(vocal_freq_signal.X_jw_shifted))
plt.title("Vocal JW Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.tight_layout()
plt.savefig(save_graph_path)
plt.close()

plt.figure(figsize=(12, 8))

# plt.subplot(2, 1, 1)
# plt.plot(t, vocal_pure_t)
# plt.title("Vocal Pure")
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude")
# plt.grid(True)

# plt.subplot(2, 1, 2)
# plt.plot(vocal_omega, vocal_pure_jw_shifted)
# plt.title("Vocal Pure JW Spectrum")
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude")
# plt.grid(True)

# plt.tight_layout()
# plt.savefig(save_graph_path.replace(".png", "_residue.png"))
# plt.close()

# 将该时域信号进行保存
vocal_time_signal.save(save_vocal_path)

print("finished")
