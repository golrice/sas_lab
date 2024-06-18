import numpy as np
from pydub import AudioSegment
from scipy.interpolate import interp1d

# 时域信号
class TimeSignal:
    # 读取wav文件
    def __init__(self, x_t=np.array([]), time_axis=np.array([])):
        self.x_t = x_t
        # 时间轴
        self.time_axis = time_axis
    
    @staticmethod
    def from_path(path):
        audio = AudioSegment.from_file(path)

        x_t = np.array(audio.get_array_of_samples())
        # 采样率
        freq = audio.frame_rate
        # 时间轴
        time_axis = np.linspace(0, len(x_t) / freq, len(x_t))

        return TimeSignal(x_t, time_axis)

    def delta_time(self):
        return self.time_axis[1] - self.time_axis[0]
    
    # 转换成频域信号
    def to_frequency(self):
        X_jw = np.fft.fft(self.x_t)
        X_jw_shifted = np.fft.fftshift(X_jw) * self.delta_time()
        omega = np.fft.fftfreq(len(self.x_t), d=self.delta_time()) * 2 * np.pi
        omega_axis = np.fft.fftshift(omega)
        return FrequencySignal(X_jw_shifted, omega_axis)

    def save(self, path):
        x_t_bytes = self.x_t.astype(np.int16)
        required_length = (x_t_bytes.size // 4) * 4  # 4 字节对应每个立体声样本帧
        # 截断或填充数据
        if x_t_bytes.size > required_length:
            x_t_bytes = x_t_bytes[:required_length]

        audio = AudioSegment(x_t_bytes, frame_rate=48000, sample_width=2, channels=2)
        audio.export(path, format="wav")

# 频域信号
class FrequencySignal:
    def __init__(self, X_jw_shifted=np.array([]), omega_axis=np.array([])):
        self.X_jw_shifted = X_jw_shifted
        self.omega_axis = omega_axis

    def delta_omega(self):
        return self.omega_axis[1] - self.omega_axis[0]

    # 转换成时域信号
    def to_time(self):
        x_t = np.fft.ifft(self.X_jw_shifted) * len(self.omega_axis) * self.delta_omega() / (2*np.pi)        
        x_t = np.real(x_t)
        t = np.fft.fftfreq(len(self.omega_axis), d=self.delta_omega()/(2*np.pi))

        return TimeSignal(x_t, t)

    def multiply(self, other):
        interp_1 = interp1d(self.omega_axis, self.X_jw_shifted, kind='cubic', fill_value='extrapolate')
        interp_2 = interp1d(other.omega_axis, other.X_jw_shifted, kind='cubic', fill_value='extrapolate')
        common_x = np.union1d(self.omega_axis, other.omega_axis)

        interp_1_values1 = interp_1(common_x)
        interp_2_values1 = interp_2(common_x)

        return FrequencySignal(interp_1_values1 * interp_2_values1, common_x)
