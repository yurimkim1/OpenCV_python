import cv2 as cv


alpha = 0.0
beta = 1.0
alpha_weight = 0.01
beta_weight = -0.01

img1 = cv.imread('beach.png', cv.IMREAD_COLOR)
img2 = cv.imread('cat.png', cv.IMREAD_COLOR)

while True:

    dst = cv.addWeighted(img1, alpha, img2, beta, 0)

    print( alpha, " ", beta)

    cv.imshow('dst',dst)
    key = cv.waitKey(33)
    if key == ord('q'):
        break
 
    alpha += alpha_weight
    beta += beta_weight

    if alpha >= 1 or alpha <= 0:
        alpha_weight = -alpha_weight
    if beta >= 1 or beta <= 0:
        beta_weight = -beta_weight

cv.destroyAllWindows()