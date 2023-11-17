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