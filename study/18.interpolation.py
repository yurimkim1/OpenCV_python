import cv2

src = cv2.imread("../img/car.png")

dst = src[280:310, 240:405]
# dst = cv2.resize(dst, dsize=(256*5, 256), interpolation=cv2.INTER_NEAREST)
dst = cv2.resize(dst, dsize=(256*5, 256), interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()