## FFt Transform


import matplotlib.pyplot as plt
import numpy
import scipy.fftpack as fftim
from scipy.misc.pilutil import Image

# opening the image and converting it to grayscale
a = Image.open('lenna.png').convert('L')
# a is converted to an ndarray
b = numpy.asarray(a)
# performing FFT
c = abs(fftim.fft2(b))
# shifting the Fourier frequency image
d = fftim.fftshift(c)

d.astype('float').tofile('fft lenna.raw')

p = numpy.fft.ifft2(d, s=None, axes=(-2,-1))
fig = plt.figure()
image1 = plt.subplot(121)
image2 = plt.subplot(122)


# put the images into the window
_ = image1.imshow(a)
_ = image2.imshow(p)


# hide axis and show window with images
image1.axis("on")
image2.axis("on")
plt.show()
