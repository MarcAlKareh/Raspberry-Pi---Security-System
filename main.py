import cv2
import time
import datetime

cap = cv2.VideoCapture(0)

# Set up the face and body cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

while True:
  _, frame = cap.read()

  # Get list of positions of faces
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.2, 5)

  for (x, y, width, height) in faces:
    cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

  cv2.imshow('Camera', frame)

  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()