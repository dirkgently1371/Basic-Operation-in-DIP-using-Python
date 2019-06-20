## Segmentation
from skimage.filters.thresholding import threshold_otsu
from scipy.misc.pilutil import Image
import scipy.misc
import matplotlib.pyplot as plt

# opening the image and converting it to grayscale
a = Image.open('spinwheel.png').convert('L')

# a is converted to an ndarray
a1 = scipy.misc.fromimage(a)

# performing Otsu's thresholdingSegmentation 143
thresh = threshold_otsu(a1)
temp = a1
# pixels with intensity greater than theshold are kept
for i in range (0 , len(temp)):
    for j in range(0 , len(temp[i])):
        if temp[i,j] < thresh:
            temp[i,j] = 0
            
# b is converted from ndimage to
b = scipy.misc.toimage(temp)

# plot
fig = plt.figure()
image1 = plt.subplot(121)
image2 = plt.subplot(122)

# put the images into the window
_ = image1.imshow(a)
_ = image2.imshow(b)

# hide axis and show window with images
image1.axis("on")
image2.axis("on")
plt.show()
