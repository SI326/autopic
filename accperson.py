import cv2
from datetime import datetime

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)   # width
cap.set(4, 480)   # height

# Load pre-trained classifier (Haar Cascade for upper body or face)
person_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
face_cascade   = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting...")
        break

    # Convert to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect people (you can switch between fullbody / face cascade)
    persons = person_cascade.detectMultiScale(gray, 1.1, 4)
    faces   = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around detections
    for (x, y, w, h) in persons:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Count people (faces used here for better accuracy with webcam)
    count = len(faces)

    # Add timestamp + count overlay
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, f"Time: {timestamp}", (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"Person Count: {count}", (10, 55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Show the result
    cv2.imshow("Webcam Person Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
