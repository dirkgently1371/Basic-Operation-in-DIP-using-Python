# Mean Filtering

import scipy.ndimage
from scipy.misc.pilutil import Image
import matplotlib.pyplot as mpl

# opening the image and converting it to grayscale
a = Image.open('lenna.png').convert('L')

# performing convolution
b = scipy.ndimage.filters.median_filter(a,size=5,mode='reflect')

# b is converted from an ndarray to an image
b = scipy.misc.toimage(b)

#b.save('meanfilter_lenna.png')

mpl.imshow(b)