## Adaptive Thresholding

from scipy.misc.pilutil import Image
import scipy.misc
import matplotlib.pyplot as plt
from skimage.filters import threshold_adaptive

# opening the image and converting it to grayscale
a = Image.open('text_sample.png').convert('L')

# a is converted to an ndarray
a1 = scipy.misc.fromimage(a)

# adaptive thresholding
block_size = 85
temp = threshold_adaptive(a1 ,block_size ,offset = 10)

# plot
fig = plt.figure()
image1 = plt.subplot(121)
image2 = plt.subplot(122)

# put the images into the window
_ = image1.imshow(a)
_ = image2.imshow(temp)

# hide axis and show window with images
image1.axis("on")
image2.axis("on")
plt.show()
