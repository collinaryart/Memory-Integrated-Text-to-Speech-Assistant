import subprocess
import os

# def install_packages():
#     try:
#         # Execute the pip install command
#         subprocess.check_call(["pip", "install", "gTTS", "speechrecognition", "pyaudio"])
#         print("Packages installed successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to install packages: {e}")

# install_packages()

from gtts import gTTS

def text_to_speech(text):
    """
    Converts the given text to speech and saves it as an mp3 file.
    """
    tts = gTTS(text=text, lang='en')
    #change the path according to your system
    filename = r"D:\opencv\sources\speech.mp3"
    tts.save(filename)
    print(f"Speech saved to {filename}")
    # This line is for playing the speech on systems with a default command for playing.
    # Modify 'start' to the appropriate command on your OS if necessary (e.g., 'open' for macOS, 'xdg-open' for Linux).
    os.system(f"start {filename}")

def read_text_from_file(filepath):
    """
    Reads text from a given file.
    """
    with open(filepath, 'r') as file:
        return file.read()

def main():
    choice = input("Enter '1' to type text manually, or '2' to read from a file: ")
    if choice == '1':
        text = input("Enter the text for speech conversion: ")
    elif choice == '2':
        filepath = input("Enter the full path to the text file: ")
        text = read_text_from_file(filepath)
    else:
        print("Invalid choice. Exiting.")
        return
    text_to_speech(text)

if __name__ == "__main__":
    main()

