import cv2

image = cv2.imread('Untitled.jpg')

gray_image = cv2.cvtColor(image, cv2. COLOR_BGR2GRAY)
resized_image = cv2.resize(gray_image, (200, 200))
cv2.imshow('Processed Image', resized_image)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('grayscale_resized_image.jpg', resized_image)
    print("Image has been saved as grayscale_resized_image.jpg")
cv2.destroyAllWindows()

print(f"Processed Image Dimenstions {resized_image.shape}")