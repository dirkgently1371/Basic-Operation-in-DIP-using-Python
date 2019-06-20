# Inverse Transform

import scipy.misc
import matplotlib.pyplot as mpl
from scipy.misc.pilutil import Image
# opening the image and converting it to grayscale92 Image Processing and Acquisition using Python
im = Image.open('lenna.png').convert('L')
# im is converted to an ndarray
im1 = scipy.misc.fromimage(im)
# performing the inversion operation
im2 = 255 - im1
# im2 is converted from an ndarray to an image
im3 = scipy.misc.toimage(im2)

mpl.imshow(im3)
