import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

image_path="img.png"
img=Image.open(image_path)
img_array = np.array(img)
red= img_array[:, :, 0]
green= img_array[:, :, 1]
blue= img_array[:, :, 2]

plt.figure(figsize=(10, 7))
plt.hist(red.flatten(), bins=256, color='red', alpha=0.5, label='Red Channel')
plt.hist(green.flatten(), bins=256, color='green', alpha=0.5, label='Green Channel')
plt.hist(blue.flatten(), bins=256, color='blue', alpha=0.5, label='Blue Channel')
plt.legend(loc='upper right')
plt.title('RGB color Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
