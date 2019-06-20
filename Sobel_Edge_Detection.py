# Sobel and Prewitt Edge Detection 

import scipy.misc
from scipy.misc.pilutil import Image
from skimage import filters
import matplotlib.pyplot as mpl

# opening the image and converting it to grayscale
a = Image.open('lenna.png').convert('L')

# performing convolution
b = filters.prewitt(a)

# b is converted from an ndarray to an image
b = scipy.misc.toimage(b)

#b.save('meanfilter_lenna.png')

mpl.imshow(b)