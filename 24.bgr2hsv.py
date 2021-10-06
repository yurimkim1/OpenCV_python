import cv2

src = cv2.imread("../img/crow.jpg")
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2YUV)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()