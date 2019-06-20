## Lowpass filtering

import scipy.misc
import numpy, math
import scipy.fftpack as fftim
from scipy.misc.pilutil import Image
import matplotlib.pyplot as plt

# opening the image and converting it to grayscale
a = Image.open('lenna.png').convert('L')

# a is converted to an ndarray
b = numpy.asarray(a)

# performing FFT
c = fftim.fft2(b)

# shifting the Fourier frequency image
d = fftim.fftshift(c)

# intializing variables for convolution function
M = d.shape[0]
N = d.shape[1]

# H is defined and values in H are initialized to 1
H = numpy.ones((M,N))
center1 = M/2
center2 = N/2

# cut-off radius122 Image Processing and Acquisition using Python
d_0 = 50.0 

# euclidean distance from origin is computed
for i in range(1,M):
    for j in range(1,N):
        r1 = (i-center1)**2+(j-center2)**2    
r = math.sqrt(r1)

# using cut-off radius to eliminate high frequency
if r > d_0:
    H[i,j] = 0.0
    
# converting H to an image
H = scipy.misc.toimage(H)

# performing the convolution
con = d * H

# computing the magnitude of the inverse FFT
e = abs(fftim.ifft2(con))

# e is converted from an ndarray to an image
f = scipy.misc.toimage(e)

# make new figure with 2 subfigures each subfigure can have an image in it
fig = plt.figure()
image1 = plt.subplot(121)
image2 = plt.subplot(122)

# put the images into the window
_ = image1.imshow(a)
_ = image2.imshow(f)

# hide axis and show window with images
image1.axis("on")
image2.axis("on")
plt.show()