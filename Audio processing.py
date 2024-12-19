
import pyaudio
import wave
import librosa
from scipy.spatial import distance

# Parameters for audio recording
FORMAT = pyaudio.paInt16  # Format for audio samples
CHANNELS = 1  # Mono channel
RATE = 44100  # Sample rate
CHUNK = 1024  # Number of frames per buffer
RECORD_SECONDS = 5  # Duration of the recording
OUTPUT_FILENAME = "output.wav"  # Output file name for recorded audio


# Create PyAudio object and audio stream
def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    return OUTPUT_FILENAME


# Feature extraction function using librosa (MFCCs)
def extract_features(audio_file):
    y, sr = librosa.load(audio_file)
    features = librosa.feature.mfcc(y=y, sr=sr)
    return features


# Function to compare two audio files based on their features
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


# Main function to record and compare audio
def main():
    # Record audio and save to WAV
    recorded_audio = record_audio()

    # Path to your reference MP3 file
    mp3_file = "C:\\Users\\ariun\\Downloads\\distant-ambulance-siren-6108.mp3"  # Update with the path to the MP3 file

    mse = compare_audio_content(recorded_audio, mp3_file)
    threshold = 0.001  # Threshold for similarity

    if mse < threshold:
        print("Ambulance is near!, be careful!")
    else:
        print("Not yet!, It's safe to move!")


if __name__ == "__main__":
    main()
