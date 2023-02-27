import cv2
import matplotlib.pyplot as plt


def blur_image(img, kernel_size=5):
    blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    return blurred


def sharpen_image(img, kernel_size=5, amount=1, threshold=0):
    blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    sharpened = cv2.addWeighted(img, 1 + amount, blurred, -amount, threshold)
    return sharpened


img = cv2.imread('test_images/0AA0A2.jpg')
blurred_img = blur_image(img)
sharpened_img = sharpen_image(img)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0].set_title('Original Image')
ax[1].imshow(cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB))
ax[1].set_title('Blurred Image')
plt.show()

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0].set_title('Original Image')
ax[1].imshow(cv2.cvtColor(sharpened_img, cv2.COLOR_BGR2RGB))
ax[1].set_title('Sharpened Image')
plt.show()
