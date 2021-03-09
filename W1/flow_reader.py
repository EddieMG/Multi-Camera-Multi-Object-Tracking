import cv2
import numpy as np


def read_flow(flow_file):
    # channels: BGR
    im = cv2.imread(flow_file, cv2.IMREAD_UNCHANGED).astype(np.double)

    # comentar una mica pq es fa això i què és im_exists
    im_u = (im[:, :, 2] - 2 ** 15) / 64
    im_v = (im[:, :, 1] - 2 ** 15) / 64

    im_exists = im[:, :, 0]
    im_exists[im_exists > 1] = 1

    im_u[im_exists == 0] = 0
    im_v[im_exists == 0] = 0

    optical_flow = np.dstack((im_u, im_v, im_exists))

    return optical_flow
