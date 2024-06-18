import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
import os

# constants
# eigenfunction 表示 频率响应
eigenfunction_path = os.path.join(os.path.dirname(__file__), "..", "resources", "eigenfunction.wav")
# vocal 表示 人声信息
vocal_path = os.path.join(os.path.dirname(__file__), "..", "resources", "vocal.wav")
save_graph_path = os.path.join(os.path.dirname(__file__), "..", "resources", "graph.png")
vocal_pure_path = os.path.join(os.path.dirname(__file__), "..", "resources", "vocal_pure.wav")

# load audio and calculate JW spectrum
eigenfunction_audio = AudioSegment.from_wav(eigenfunction_path)
eigenfunction_array = np.array(eigenfunction_audio.get_array_of_samples())
eigenfunction_freq = eigenfunction_audio.frame_rate
eigenfunction_time = np.linspace(0, len(eigenfunction_array) / eigenfunction_freq, len(eigenfunction_array))
eigenfunction_delta_t = eigenfunction_time[1] - eigenfunction_time[0]

eigenfunction_jw = np.fft.fft(eigenfunction_array)
eigenfunction_jw_shifted = np.fft.fftshift(eigenfunction_jw) * eigenfunction_delta_t

eigenfunction_omega = np.fft.fftfreq(len(eigenfunction_array), d=eigenfunction_delta_t) * 2 * np.pi

vocal_audio = AudioSegment.from_wav(vocal_path)
vocal_array = np.array(vocal_audio.get_array_of_samples())
vocal_freq = vocal_audio.frame_rate
vocal_time = np.linspace(0, len(vocal_array) / vocal_freq, len(vocal_array))
vocal_delta_t = vocal_time[1] - vocal_time[0]

vocal_jw = np.fft.fft(vocal_array)
vocal_jw_shifted = np.fft.fftshift(vocal_jw) * vocal_delta_t

vocal_omega = np.fft.fftfreq(len(vocal_array), d=vocal_delta_t) * 2 * np.pi
vocal_delta_omega = vocal_omega[1] - vocal_omega[0]

# LTI transform
# 使用上面得到的eigenfunction和vocal的JW频谱，进行LTI变换
# S(jw) = eigenfunction_jw_shifted
# X(jw) = vocal_jw_shifted
# vocal_pure_jw = X(jw) * S(jw)
# 需要构造出 H(jw)

# plot graphs
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(eigenfunction_time, eigenfunction_array)
plt.title("Eigenfunction")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(vocal_time, vocal_array)
plt.title("Vocal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(eigenfunction_omega, np.abs(eigenfunction_jw_shifted))
plt.title("Eigenfunction JW Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(vocal_omega, np.abs(vocal_jw_shifted))
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

print("finished")
