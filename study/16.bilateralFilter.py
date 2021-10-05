import cv2

src = cv2.imread("../img/crescent.jpg")
cv2.imshow("src", src)

dst = cv2.blur(src,(5,5))
# dst = cv2.GaussianBlur(src,(5,5),2)
# 엣지는 보존하고 엣지가 아닌 곳은 블러링 효과
# dst = cv2.bilateralFilter(src, 100, 33, 11, borderType=cv2.BORDER_ISOLATED)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()