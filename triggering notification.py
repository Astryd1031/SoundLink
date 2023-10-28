from pydub import AudioSegment
import os
import subprocess

# Path to the audio file
audio_file_path = 'path_to_audio_file.mp3'

# Desired duration limit in milliseconds
duration_limit = 60000  # 60 seconds

# Check the duration of the audio file
audio = AudioSegment.from_file(audio_file_path)
audio_duration = len(audio)

if audio_duration > duration_limit:
    # Trigger a notification
    notification_message = f"Audio duration exceeded {duration_limit / 1000} seconds."
    print(notification_message)

    # You can also use other notification methods here, like sending an email or using a notification service

# Optionally, you can use a system-specific method to trigger notifications, e.g., on macOS
if os.name == 'posix':
    subprocess.run(["osascript", "-e", f'display notification "{notification_message}" with title "Audio Notification"'])
