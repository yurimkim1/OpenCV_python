import numpy as np
import cv2

src = cv2.imread('../img/psycho_but_okay.jpeg', cv2.IMREAD_COLOR)

val = 100
array = np.full(src.shape, (val, val, val), dtype=np.uint8)

add_dst = cv2.add(src, array)
sub_dst = cv2.subtract(src, array)

cv2.imshow('src', src)
cv2.imshow('add_dst', add_dst)
cv2.imshow('sub_dst', sub_dst)

cv2.waitKey()
cv2.destroyAllWindows()