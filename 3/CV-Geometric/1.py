import cv2
import numpy as np

image = np.ones((512, 512, 3), dtype=np.uint8) * 255

cv2.circle(image, (80, 80), 40, (0, 255, 255), -1)

cv2.line(image, (80, 20), (80, 50), (0, 255, 255), 3)
cv2.line(image, (80, 110), (80, 140), (0, 255, 255), 3)
cv2.line(image, (20, 80), (50, 80), (0, 255, 255), 3)
cv2.line(image, (110, 80), (140, 80), (0, 255, 255), 3)


cv2.line(image, (150, 350), (360, 350), (0, 0, 0), 5)
cv2.line(image, (150, 350), (200, 380), (0, 0, 0), 5)
cv2.line(image, (360, 350), (310, 380), (0, 0, 0), 5)


cv2.line(image, (255, 350), (255, 200), (0, 0, 0), 5)


cv2.line(image, (255, 200), (180, 300), (0, 0, 0), 4)
cv2.line(image, (180, 300), (255, 300), (0, 0, 0), 4)
cv2.line(image, (255, 300), (255, 200), (0, 0, 0), 4)


cv2.imshow("1", image)
cv2.waitKey(0)
cv2.destroyAllWindows()