from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('Shreyas.jpeg'))
lum_img = img[:, :, 0]

plt.imshow(lum_img, cmap="hot")


'''
img = Image.open('Shreyas.jpeg')
img.thumbnail((64, 64))  # resizes image in-place
imgplot = plt.imshow(img)
'''
plt.colorbar()
plt.show()


