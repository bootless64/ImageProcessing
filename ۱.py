
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
