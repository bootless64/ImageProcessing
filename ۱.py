فیلتر (میانگین‌گیر برای کاهش نویز)
filtered = cv2.medianBlur(corrected, 5)

# 4. Morphology - انتخاب structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))

# اعمال Top-hat (برای برجسته‌سازی اجسام روشن روی پس‌زمینه تیره)
morph_result = cv2.morphologyEx(filtered, cv2.MORPH_TOPHAT, kernel)

# 5. Threshold
_, thresh = cv2.threshold(morph_result, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 6. Edge Detection
edges = cv2.Canny(thresh, 50, 150)

# نمایش نتایج
titles = ['Original', 'Background Corrected', 'Filtered', 'Top-hat Result', 'Threshold', 'Edges']
images = [img, corrected, filtered, morph_result, thresh, edges]

plt.figure(figsize=(15, 10))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
