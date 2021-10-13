import cv2 as cv


img_color = cv.imread('square.png', cv.IMREAD_COLOR)


img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)


kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)


contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, 
                        cv.CHAIN_APPROX_SIMPLE)


cv.drawContours(img_color, contours, 0, (0, 0, 255), 3)  


for contour in contours:

    epsilon = 0.03 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)

    cv.drawContours(img_color, [approx], 0, (0, 255, 0), 3)


cv.imshow("result", img_color)
cv.waitKey(0)