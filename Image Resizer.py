import cv2

image = cv2.imread('Untitled.jpg')

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
small_image = cv2.resize(image, (200, 200))
medium_image = cv2.resize(image, (500, 500))
large_image = cv2.resize(image, (1000, 1000))
cv2.imshow('Normal', image)
cv2.imshow('Small Image', small_image)
cv2.imshow('Medium Image', medium_image)
cv2.imshow('Large Image', large_image)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('small image.jpg', small_image)
    cv2.imwrite('medium image.jpg', medium_image)
    cv2.imwrite('large image.jpg', large_image)
    print("Saved!")
cv2.destroyAllWindows()