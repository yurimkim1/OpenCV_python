import numpy as np
import cv2

src = cv2.imread("../img/clouds.jpg")
height, width, _ = src.shape

src_pts = np.array([[0.0, 0.0], [width, 0.0], [width, height], [0.0, height]], dtype=np.float32)
dst_pts = np.array([[300.0, 300.0], [900.0, 200.0], [width-100.0, height-100.0], [0.0, height-200.0]], dtype=np.float32)

M = cv2.getPerspectiveTransform(src_pts, dst_pts)

dst = cv2.warpPerspective(src, M, (width, height), borderValue=(255, 255, 255, 0))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

