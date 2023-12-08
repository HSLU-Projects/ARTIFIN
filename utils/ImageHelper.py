import math
import cv2
import numpy as np


@staticmethod
def calculate_bounding_box(x, y, width, height):
    x0 = x - width / 2
    x1 = x + width / 2
    y0 = y - height / 2
    y1 = y + height / 2
    start_point = (int(x0), int(y0))
    end_point = (int(x1), int(y1))
    return start_point, end_point


@staticmethod
def crop_image(image, start_point, end_point):
    return image[int(start_point[1]):int(end_point[1]), int(start_point[0]):int(end_point[0])]


@staticmethod
def find_rotation_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = -(y2 - y1)

    alpha = math.degrees(math.atan2(dy, dx))
    return 90-alpha


@staticmethod
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # rotate our image around the center of the image
    M = cv2.getRotationMatrix2D((cX, cY), angle-180, 1.0)
    return cv2.warpAffine(image, M, (w, h))


@staticmethod
def centre_image(image, x, y):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    (dx, dy) = (x - cX, y - cY)
    # translate the image
    M = np.float32([
        [1, 0, -dx],
        [0, 1, -dy]
    ])
    return cv2.warpAffine(image, M, (w, h))
