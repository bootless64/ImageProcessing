import cv2
import numpy as np

# ------------------------------
# 0. بارگذاری تصویر
# ------------------------------
img = cv2.imread("doca.jpeg", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("تصویر پیدا نشد!")

cv2.imshow("Original", img)
cv2.waitKey(0)

# ------------------------------
# 1. Edge Detection برای تخمین زاویه
# ------------------------------
edges = cv2.Canny(img, 50, 150)

# ------------------------------
# 2. Hough Lines برای تخمین Skew
# ------------------------------
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
angles = []

if lines is not None:
    for line in lines:
        rho, theta = line[0]
        angle = (theta * 180 / np.pi) - 90  # تبدیل به درجه
        angles.append(angle)

# میانه زاویه‌ها برای دقت بهتر
if len(angles) > 0:
    skew_angle = np.median(angles)
else:
    skew_angle = 0

print("Skew angle:", skew_angle)

# ------------------------------
# 3. Rotation (Geometric Transform)
# ------------------------------
h, w = img.shape
M = cv2.getRotationMatrix2D((w//2, h//2), skew_angle, 1)
rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

cv2.imshow("Rotated", rotated)
cv2.waitKey(0)

# ------------------------------
# 4. Gaussian Blur برای کاهش نویز
# ------------------------------
blur = cv2.GaussianBlur(rotated, (5,5), 0)

# ------------------------------
# 5. Adaptive Threshold
# ------------------------------
binary = cv2.adaptiveThreshold(
    blur,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    25,
    10
)

cv2.imshow("Binary", binary)
cv2.waitKey(0)

# ------------------------------
# 6. Morphology (Close/Open)
# ------------------------------
kernel = np.ones((3,3), np.uint8)
morph = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

cv2.imshow("Morphology", morph)
cv2.waitKey(0)

# ------------------------------
# 7. Bitwise AND برای ماسک کردن نویز
# ------------------------------
result = cv2.bitwise_and(rotated, rotated, mask=morph)

cv2.imshow("Deskewed Text", result)
cv2.waitKey(0)
cv2.destroyAllWindows()