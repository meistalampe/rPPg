import cv2
import numpy as np
import sys

"""
Landmark Regions
0-16 = Jawline
17-21 = Right Eyebrow
22-26 = Left Eyebrow
27-35 = Nose
36-41 = Right Eye
42-47 = Left Eye
48-60 = Lips (outer perimeter)
61-67 = Lips (inner perimeter)
"""


def get_roi_from_landmarks_forehead(_predictions: list):
    if len(_predictions) != 68:
        print("Input does not meet size requirement. Expected input: list, length=68.")
        sys.exit(1)
    else:
        pass

    # forehead roi consists of 4 points
    x1 = int(_predictions[20][0])
    y1 = int(_predictions[20][1] - 10)
    x2 = int(_predictions[23][0])
    y2 = int(_predictions[23][1] - 10)
    x3 = int(_predictions[23][0])
    y3 = int(_predictions[23][1] - 35)
    x4 = int(_predictions[20][0])
    y4 = int(_predictions[20][1] - 35)
    points = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    return points


def draw_roi(_roi_points: list, _image: np.ndarray, _color: tuple = (255, 0, 255), _thickness: int = 1):
    roi_points = np.array(_roi_points, dtype=np.int32)
    final_points = roi_points.reshape((-1, 1, 2))
    cv2.polylines(_image, [final_points], True, color=_color, thickness=_thickness)


def get_values_from_roi(_roi_points: list, _image):
    mask = np.zeros((_image.shape), dtype=np.uint8)

    # define points (as small diamond shape)
    pts = np.array([_roi_points], dtype=np.int32)
    cv2.fillPoly(mask, pts, (255, 255, 255))

    # get color values
    values = _image[np.where((mask == (255, 255, 255)).all(axis=2))]
    # print(values)
    return values

