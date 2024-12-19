# SoundLink: Real-Time Audio Recognition

**SoundLink** is a real-time audio recognition system that listens to the microphone, compares the captured sound with a predefined reference audio file (e.g., an ambulance siren), and provides an alert if the sound is detected. The system can also perform speech recognition in real time using advanced libraries like `librosa`, `pyaudio`, and `speech_recognition`.

## Features
- **Real-time Audio Capture**: Captures live audio from the microphone.
- **Sound Detection**: Compares recorded audio with a predefined reference sound (e.g., an ambulance siren).
- **Speech Recognition**: Recognizes speech from the recorded audio.
- **Threshold-Based Detection**: Provides alerts when the detected audio is similar to a reference sound based on feature comparison (MFCC).
- **Extensibility**: Can be extended to detect various sounds or keywords in real-time.

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. You will also need to install the following dependencies:

```bash
pip install pyaudio speechrecognition librosa scipy numpy
```

### Installation Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/SoundLink.git
   ```

2. **Install dependencies**:

   ```bash
   cd SoundLink
   pip install -r requirements.txt
   ```

3. **Set up your reference audio**:
   - Place the reference audio file (e.g., an ambulance siren in `.mp3` format) in the appropriate directory, or update the file path in the script.

## Usage

### Run the Real-Time Audio Recognition

To run the real-time audio recognition, execute the script:

```bash
python real_time_recognizing.py
```

The system will start listening to your microphone, compare the captured audio with a reference sound, and alert you if the sound matches the reference (e.g., "Ambulance detected! Be careful!").

### Configuration
You can adjust the following parameters in the `real_time_recognizing.py` script:
- **`RECORD_SECONDS`**: Duration for each audio recording (in seconds).
- **`THRESHOLD`**: Threshold for comparing audio similarity.
- **`MP3_REFERENCE_FILE`**: Path to your reference audio file (e.g., an ambulance siren).

### Speech Recognition
The system will also attempt to recognize speech in the audio stream. Recognized speech will be printed in the console. You can modify this behavior or extend it to trigger actions based on specific keywords.

## Example Output

```bash
Real-time audio recognition started. Listening...
MSE: 0.000532
Ambulance detected! Be careful!
Recognized Speech: Help, there's an emergency!
```

## Contributing

We welcome contributions! If you'd like to contribute to **SoundLink**, please fork the repository, create a branch for your changes, and submit a pull request.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write your code and ensure all tests pass.
4. Submit a pull request with a description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
