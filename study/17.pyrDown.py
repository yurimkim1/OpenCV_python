import cv2

src = cv2.imread("../img/ferris-wheel.jpg")
dst = src.copy()

for i in range(3):
    dst = cv2.pyrDown(dst)

dst1 = dst.copy()
for i in range(3):
    dst1 = cv2.pyrUp(dst1)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst1", dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()