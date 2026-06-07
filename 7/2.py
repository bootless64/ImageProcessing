import cv2
import numpy as np

# خواندن تصویر
img = cv2.imread("images.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("تصویر پیدا نشد")

# ------------------------
# 1. Median Filter
# ------------------------
median = cv2.medianBlur(img, 5)

# ------------------------
# 2. Closing
# جلوگیری از قطع شدن ترک‌ها
# ------------------------
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (3,3)
)

closed = cv2.morphologyEx(
    median,
    cv2.MORPH_CLOSE,
    kernel,
    iterations=1
)

# ------------------------
# 3. Adaptive Threshold
# ------------------------
binary = cv2.adaptiveThreshold(
    closed,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    31,
    5
)

# ------------------------
# 4. Opening
# حذف نویزهای کوچک
# ------------------------
opened = cv2.morphologyEx(
    binary,
    cv2.MORPH_OPEN,
    kernel,
    iterations=1
)

# ------------------------
# 5. Dilation کوچک
# اتصال ترک‌های شکسته
# ------------------------
opened = cv2.dilate(
    opened,
    kernel,
    iterations=1
)

# ------------------------
# 6. Edge Detection
# ------------------------
edges = cv2.Canny(
    opened,
    50,
    150
)

# ------------------------
# نمایش نتایج
# ------------------------
cv2.imshow("Original", img)
cv2.imshow("Median", median)
cv2.imshow("Threshold", binary)
cv2.imshow("Crack Mask", opened)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()