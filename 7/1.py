import cv2
import numpy as np

# ----------- مرحله 0: بارگذاری تصویر -------------
# مسیر تصویر خود را دقیق وارد کنید
img = cv2.imread("coin.jpeg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("تصویر پیدا نشد. مسیر را چک کنید!")

cv2.imshow("Original", img)
cv2.waitKey(0)

# ----------- مرحله 1: Background Correction -------------
# Top-Hat برای برجسته کردن اجسام روشن روی پس‌زمینه تاریک و ناهمگن
# SE (structuring element) دایره‌ای و کمی بزرگ‌تر از جزئیات پس‌زمینه
kernel_size = 31  # می‌توانید با توجه به اندازه سکه تغییر دهید
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Top-Hat", tophat)
cv2.waitKey(0)

# ----------- مرحله 2: Filter (کاهش نویز) -------------
blur = cv2.GaussianBlur(tophat, (5,5), 0)
cv2.imshow("Gaussian Blur", blur)
cv2.waitKey(0)

# ----------- مرحله 3: Threshold -------------
# Otsu threshold بعد از Top-Hat و Blur بهترین عملکرد را دارد
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)

# ----------- مرحله 4: Morphology -------------
# Closing برای پر کردن سوراخ‌های داخل سکه‌ها و Open برای حذف نویز کوچک
morph_kernel = np.ones((5,5), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, morph_kernel)
morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, morph_kernel)
cv2.imshow("Morphology", morph)
cv2.waitKey(0)

# ----------- مرحله 5: Contours / Edge Detection -------------
# یافتن کانتور برای شمارش سکه‌ها
contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("amount of coins", len(contours))

# رسم کانتور روی تصویر اصلی
result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(result, contours, -1, (0,255,0), 2)

cv2.imshow("Coins Detected", result)
cv2.waitKey(0)
cv2.destroyAllWindows()