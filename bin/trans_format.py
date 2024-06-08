import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

# constants
audio_eigenfunction = "resources/eigenfunction.acc"
audio_vocal = "resources/vocal.acc"

output_eigenfunction = "resources/eigenfunction.wav"
output_vocal = "resources/vocal.wav"

audios = [AudioSegment.from_file(audio_eigenfunction, format="aac"), AudioSegment.from_file(audio_vocal, format="aac")]

audios[0].export(output_eigenfunction, format="wav")
audios[1].export(output_vocal, format="wav")
