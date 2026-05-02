import cv2
import os

image_path="C:\\image.png"

if not os.path.exists(image_path):
    print(f"Error: the file at {image_path} does not exist")
else:
    image=cv2.imread(image_path,1)
    if image is None:
        print("can't open file")
    else:
        cv2.imshow("asdfghjkl",image)
        cv2.imwrite("newImg.jpg",image)

cv2.waitKey()
cv2.destroyAllWindows()
