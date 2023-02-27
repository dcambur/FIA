import cv2


def is_passport_photo(image):
    # Check if the image is colored
    if len(image.shape) < 3 or image.shape[2] < 3:
        return False

    # Check if the image is in portrait or square orientation
    (height, width, _) = image.shape
    if height > width:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        (height, width, _) = image.shape
    if height != width:
        return False

    # Detect the eyes in the image
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    if len(eyes) != 2:
        return False

    # Check if the eyes are at the same level
    (eye1_x, eye1_y, eye1_w, eye1_h) = eyes[0]
    (eye2_x, eye2_y, eye2_w, eye2_h) = eyes[1]
    eye1_center = eye1_y + (eye1_h / 2)
    eye2_center = eye2_y + (eye2_h / 2)
    if abs(eye1_center - eye2_center) > 5:
        return False

    # Check if the photo contains only one person
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    if len(faces) != 1:
        return False

    # Check if the head of the person represents 20% to 50% of the area of the photo
    (x, y, w, h) = faces[0]
    face_area = w * h
    image_area = width * height
    if face_area < (0.2 * image_area) or face_area > (0.5 * image_area):
        return False

    # If all checks pass, the photo is accepted
    return True
