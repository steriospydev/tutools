import os
import sys
from PIL import Image
import cv2

"""
Requirements:
    pillow
    opencv-python
"""
def convert_to_jpg(image_path:str) -> None:
    if os.path.exists(image_path):
      im = Image.open(image_path)
      target_name = image_path + ".jpg"
      rgb_im = im.convert("RGB")
      rgb_im.save(target_name)
      print("Saved as " + target_name)
    else:
        print(image_path + " not found.")

def sketch_image(image):
  # convert RGB image to grayscale
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  inverted_image = 255 - gray_image
  #  mixing the grayscale image with the inverted blurry image.
  blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
  inverted_blurred = 255 - blurred
  pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
  return pencil_sketch

def bilateral(image):
  median = cv2.medianBlur(image, 5)
  blur = cv2.bilateralFilter(image, 9, 75, 75)
  return blur, median

def display_img(image, sketch, blur, median):
  cv2.imshow("Original Image", image)
  cv2.imshow("Pencil Sketch", sketch)
  cv2.imshow("Bilateral Filtering", blur)
  cv2.imshow("Median Filtering", median)
  cv2.waitKey(0)


if __name__ == '__main__':
    image = cv2.imread("test.jpg")
    sketch = sketch_image(image)
    bila, median = bilateral(image)
    display_img(image, sketch, bila, median)