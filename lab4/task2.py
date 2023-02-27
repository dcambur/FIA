import cv2


def detect_face(image):
    # Load the pre-trained face detection classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Check if a face is detected
    if len(faces) > 0:
        # Assume that the image contains only one face
        # Return the coordinates of the detected face
        (x, y, w, h) = faces[0]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("img", img)
        cv2.waitKey()
        return x, y, x + w, y + h
    else:
        # If no faces are detected, return None
        return None


img = cv2.imread('test_images/0AA0A2.jpg')
face = detect_face(img)
