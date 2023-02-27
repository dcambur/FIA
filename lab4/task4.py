import cv2
import csv
from task3 import is_passport_photo
from task1 import blur_image, sharpen_image
test_folder = "test_images/"
test_csv_file = "test.csv"

# Read the labels from the test.csv file
with open(test_csv_file, "r") as f:
    reader = csv.DictReader(f)
    labels = {row['new_path']: row['label'] == 'True' for row in reader}

# Test the passport photo validator on each image in the test set
correct = 0
total = 0
for image_path, label in labels.items():
    image = cv2.imread(image_path)
    blur = blur_image(image)
    sharp = sharpen_image(blur)
    if is_passport_photo(sharp) == label:
        correct += 1
    total += 1

accuracy = correct / total
print(f"Accuracy: {accuracy:.2%}")
