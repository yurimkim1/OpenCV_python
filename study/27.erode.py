import cv2

src = cv2.imread("../img/dandelion.jpg", cv2.IMREAD_GRAYSCALE)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5), anchor=(-1, 1))
dst_erode = cv2.erode(src, kernel, iterations=3)
dst_dilte = cv2.dilate(src, kernel, iterations=3)

cv2.imshow("kernel", kernel)
cv2.imshow("dst_erode", dst_erode)
cv2.imshow("dst_dilte", dst_dilte)
cv2.waitKey(0)
cv2.destroyAllWindows()
