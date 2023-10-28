# Hello! It's team 4
# Here is the simplest prototype of our product.
# For this simple toy you can check recording audio with whatever audio that has .mp3 extension
# Note that our demo is highly ideal, meaning only with exact sound recognition, it will work.
# We need future developments needed to make this prototype a working application,
# thus, we included pseudo-code for future development.
# All rights served.
# Work by @astrydzaya


from pydub import AudioSegment
import os
import pyaudio
import wave
import ffmpeg
import soundfile as sf
from scipy.spatial import distance
# Set the parameters for audio recording
FORMAT = pyaudio.paInt16  # Format for audio samples
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # 20mber of frames per buffer
RECORD_SECONDS = 5  # Duration of the recording in seconds
OUTPUT_FILENAME = "output.wav"  # Output .wav file name

# Create a PyAudio object
audio = pyaudio.PyAudio()

# Create an audio stream for recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Record audio data
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# Close the audio stream
stream.stop_stream()
stream.close()

# Terminate the PyAudio object
audio.terminate()

# Save the recorded audio to a .wav file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))



import librosa

def extract_features(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)

    # Extract audio features (e.g., MFCCs)
    features = librosa.feature.mfcc(y=y, sr=sr)

    return features

def compare_audio_content(file1, file2):
    # Extract features from both audio files
    try:
        features1 = extract_features(file1)
        features2 = extract_features(file2)

        euclidean_dist_mfcc = distance.euclidean(features2, features1)
        mse = euclidean_dist_mfcc
    except ValueError:
        mse =0.0012


    # Compare the extracted features (you can use various methods for this)
    # For example, you can calculate the mean squared error (MSE) between the features.

    return mse

wav_file = 'output.wav'
mp3_file = "C:\\Users\\ariun\\Downloads\\distant-ambulance-siren-6108.mp3"# replace this with any .mp3 file to try!

mse = compare_audio_content(wav_file, mp3_file)

# You can define a threshold for MSE to determine if the content is similar or different.
threshold = 0.001

if mse < threshold:
    print("Ambulance is near!, be careful!")
else:
    print("Not yet!, It's safe to move!")


