import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

# 定义常量
audio_path = "/root/workingDir/sas_lab/resources/large-underwater-explosion-190270.mp3"

# 加载音频
audio = AudioSegment.from_file(audio_path)
# 基本信息
print("Sample rate:", audio.frame_rate)
print("Number of channels:", audio.channels)
print("Duration:", audio.duration_seconds)

# 转换成 numpy 数组
samples = np.array(audio.get_array_of_samples())
freq = audio.frame_rate

time_axis = np.linspace(0, len(samples) / freq, len(samples))
delta_t = time_axis[1] - time_axis[0]

# fft 变换
X_jw = np.fft.fft(samples) 
X_jw_shifted = np.fft.fftshift(X_jw) * delta_t

omega = np.fft.fftfreq(len(samples), d=delta_t) * 2 * np.pi
delta_omega = omega[1] - omega[0]
omega_shifted = np.fft.fftshift(omega)

# 假设一个系统的系统函数是X_jw_shifted
# 反变换
x_t = np.fft.ifft(X_jw_shifted * X_jw_shifted) * len(omega) * delta_omega / (2 * np.pi)
x_t = np.real(x_t)
t = np.fft.fftfreq(len(omega), d=delta_omega / (2 * np.pi))

# 显示波形
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(time_axis, samples)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(2, 2, 2)
plt.plot(t, x_t)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(omega_shifted, np.abs(X_jw_shifted))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.savefig("waveform.png")
plt.close()

# 导出音频
x_t_bytes = x_t.astype(np.int16)
# 加载音频数据为 AudioSegment 对象
audio = AudioSegment(x_t_bytes.tobytes(), frame_rate=audio.frame_rate, sample_width=2, channels=2)

# 导出为 MP3 文件
audio.export("output_audio.mp3", format="mp3")
