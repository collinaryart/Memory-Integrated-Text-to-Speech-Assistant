import cv2
import face_recognition
import numpy as np
import os

# Uncomment the following lines if you want to install the packages and comment them back once installed.

# import subprocess

# def install_packages():
#     try:
#         # Execute the pip install command
#         subprocess.check_call(["pip", "install", "opencv-python", "face_recognition", "numpy"])
#         print("Packages installed successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to install packages: {e}")

# install_packages()


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
known_face_encodings = []
known_face_names = []

# Load a sample picture and learn how to recognize it.
def load_known_faces():
    for filename in os.listdir('known_faces'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Load each file
            known_face = face_recognition.load_image_file(f'known_faces/{filename}')
            # Get the encoding of the face
            known_face_encoding = face_recognition.face_encodings(known_face)[0]
            # Use the filename without extension as the name
            known_face_names.append(filename[:-4])
            known_face_encodings.append(known_face_encoding)

load_known_faces()

# Initialize the video capture object
video_capture = cv2.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Find all faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
