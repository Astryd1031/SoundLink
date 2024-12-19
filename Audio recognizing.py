import pyaudio
import speech_recognition as sr
from scipy.spatial import distance
import librosa
import numpy as np
import time

# Parameters for audio recording
FORMAT = pyaudio.paInt16  # Format for audio samples
CHANNELS = 1  # Mono channel
RATE = 44100  # Sample rate
CHUNK = 1024  # Number of frames per buffer
RECORD_SECONDS = 5  # Duration of the recording (in seconds)
THRESHOLD = 0.001  # Threshold for determining if the audio is similar to the reference
MP3_REFERENCE_FILE = "C:\\Users\\ariun\\Downloads\\distant-ambulance-siren-6108.mp3"  # Update with the path to your reference MP3 file

# Initialize the recognizer
recognizer = sr.Recognizer()


# Function to extract features using librosa (MFCCs)
def extract_features(audio_file):
    y, sr = librosa.load(audio_file)
    features = librosa.feature.mfcc(y=y, sr=sr)
    return features


# Function to compare two audio files based on their MFCC features
def compare_audio_content(file1, file2):
    try:
        features1 = extract_features(file1)
        features2 = extract_features(file2)
        # Compare using Euclidean distance
        euclidean_dist_mfcc = distance.euclidean(features1.mean(axis=1), features2.mean(axis=1))
        mse = euclidean_dist_mfcc
    except ValueError:
        mse = 0.0012  # In case of error, set a small threshold value
    return mse


# Function to recognize speech from live audio stream
def recognize_audio_from_stream(stream):
    with sr.AudioData(stream, RATE, 2) as audio_data:
        try:
            # Recognize speech using Google Web Speech API
            print("Recognizing...")
            text = recognizer.recognize_google(audio_data)
            print(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
            return None


# Function for real-time audio recognition and comparison
def real_time_audio_recognition():
    # Initialize PyAudio for real-time audio capture
    p = pyaudio.PyAudio()

    # Open audio stream for microphone input
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Real-time audio recognition started. Listening...")

    while True:
        frames = []
        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        # Convert frames into audio data
        audio_data = b''.join(frames)

        # Save the captured audio as a temporary WAV file
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_data)

        # Compare the recorded audio with the reference (ambulance siren)
        mse = compare_audio_content("temp_audio.wav", MP3_REFERENCE_FILE)
        print(f"MSE: {mse}")

        if mse < THRESHOLD:
            print("Ambulance detected! Be careful!")
        else:
            print("No matching sound detected.")

        # Recognize speech (if any) from the captured audio
        recognized_text = recognize_audio_from_stream(audio_data)
        if recognized_text:
            print(f"Recognized Speech: {recognized_text}")

        # Add a small delay to avoid overload
        time.sleep(1)

    # Close the audio stream when done
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    real_time_audio_recognition()
