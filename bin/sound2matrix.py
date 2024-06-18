import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
import os

# constants
# eigenfunction 表示 频率响应
eigenfunction_path = os.path.join(os.path.dirname(__file__), "..", "resources", "eigenfunction.wav")
# 保存波形数据矩阵地址
eigenfunction_matrix_path = os.path.join(os.path.dirname(__file__), "..", "resources", "soundmatrix", "eigenfunction_matrix.npy")
# vocal 表示 人声信息
vocal_path = os.path.join(os.path.dirname(__file__), "..", "resources", "vocal.wav")
vocal_matrix_path = os.path.join(os.path.dirname(__file__), "..", "resources", "soundmatrix", "vocal_matrix.npy")
# vocal_pure 表示 去除人声信息后的音频
vocal_pure_path = os.path.join(os.path.dirname(__file__), "..", "resources", "vocal_pure.wav")
vocal_pure_matrix_path = os.path.join(os.path.dirname(__file__), "..", "resources", "soundmatrix", "vocal_pure_matrix.npy")

eigenfunction_audio = AudioSegment.from_wav(eigenfunction_path)
vocal_audio = AudioSegment.from_wav(vocal_path)
vocal_pure_audio = AudioSegment.from_wav(vocal_pure_path)

print(f"type of eigenfunction_audio: {type(eigenfunction_audio)}")
print(f"type of vocal_audio: {type(vocal_audio)}")
print(f"type of vocal_pure_audio: {type(vocal_pure_audio)}")

# 将对应音频的波形数据转换为矩阵
eigenfunction_matrix = np.array(eigenfunction_audio.get_array_of_samples()).reshape((-1, 2))
vocal_matrix = np.array(vocal_audio.get_array_of_samples()).reshape((-1, 2))
vocal_pure_matrix = np.array(vocal_pure_audio.get_array_of_samples()).reshape((-1, 2))

# 保存矩阵
np.save(eigenfunction_matrix_path, eigenfunction_matrix)
np.save(vocal_matrix_path, vocal_matrix)
np.save(vocal_pure_matrix_path, vocal_pure_matrix)

print("save matrix successfully!")

# 读取矩阵
eigenfunction_matrix2 = np.load(eigenfunction_matrix_path)
vocal_matrix2 = np.load(vocal_matrix_path)
vocal_pure_matrix2 = np.load(vocal_pure_matrix_path)

# 检查矩阵是否正确读取
print(f"eigenfunction_matrix2: {eigenfunction_matrix2.shape}, {eigenfunction_matrix2.dtype}")
print(f"vocal_matrix2: {vocal_matrix2.shape}, {vocal_matrix2.dtype}")
print(f"vocal_pure_matrix2: {vocal_pure_matrix2.shape}, {vocal_pure_matrix2.dtype}")
# 检查元素是否相同
print(f"eigenfunction equal:{np.array_equal(eigenfunction_matrix, eigenfunction_matrix2)}")
print(f"vocal equal:{np.array_equal(vocal_matrix, vocal_matrix2)}")
print(f"vocal_pure equal:{np.array_equal(vocal_pure_matrix, vocal_pure_matrix2)}")
