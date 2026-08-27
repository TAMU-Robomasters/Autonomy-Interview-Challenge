import numpy as np

dist = np.load("calibration/dist.pkl", allow_pickle=True)
cam_matrix = np.load("calibration/cameraMatrix.pkl", allow_pickle=True)

# height is 5.9 cm, width is 13.8 cm
panel_coordinates = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
], dtype=np.float32)