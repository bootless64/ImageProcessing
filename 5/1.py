import cv2
import numpy as np

#Question 1
image=np.ones((300, 300), dtype=np.uint8)

# cv2.imshow("Rectangle", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Question 2 && 3






a=cv2.imread("images/1.png")
b=cv2.imread("images/2.jpg")
image1=cv2.resize(a,(300,300))
image2=cv2.resize(b,(300,300))
image3=cv2.resize(a,(300,300))

bitwise_and = cv2.bitwise_and(image1, image2)
bitwise_or = cv2.bitwise_or(image1, image2)
bitwise_xor = cv2.bitwise_xor(image1, image2)
bitwise_not_image1 = cv2.bitwise_not(image1)
bitwise_not_image2 = cv2.bitwise_not(image2)

cv2.putText(image3,"You are invited",(40,40),cv2.FONT_HERSHEY_TRIPLEX,0.9,(0,0,255))

cv2.imshow("text ", image3)
cv2.imshow("card", image1)
cv2.imshow("flower", image2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("XOR", bitwise_xor)
cv2.imshow("NOT - card", bitwise_not_image1)
cv2.imshow("NOT - flower", bitwise_not_image2)

cv2.circle(image2, (150, 150), 100, (0, 255, 0), -1)

cv2.waitKey(0)
cv2.destroyAllWindows()