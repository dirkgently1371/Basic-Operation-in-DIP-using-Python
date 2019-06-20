## Butterworth filter

import numpy, math
import scipy.misc
import scipy.fftpack as fftim
from scipy.misc.pilutil import Image
import matplotlib.pyplot as plt

# opening the image and converting it to grayscale
a = Image.open('lenna.png').convert('L')

# a is converted to an ndarray
b = numpy.array(a)

# performing FFT
c = fftim.fft2(b)

# shifting the Fourier frequency image124 Image Processing and Acquisition using Python
d = fftim.fftshift(c)

# intializing variables for convolution function
M = d.shape[0]
N = d.shape[1]

# H is defined and values in H are initialized to 1
H = numpy.ones((M,N))
center1 = M/2
center2 = N/2
d_0 = 30.0 # cut-off radius
t1 = 1 # the order of BLPF
t2 = 2*t1

# defining the convolution function for BLPF
for i in range(1,M):
    for j in range(1,N):
        r1 = (i-center1)**2+(j-center2)**2
        
# euclidean distance from origin is computed
r = math.sqrt(r1)

# using cut-off radius to eliminate high frequency
if r > d_0:
    H[i,j] = 1/(1 + (r/d_0)**t1)
    
# converting H to an image
H = scipy.misc.toimage(H)

# performing the convolution
con = d * H

# computing the magnitude of the inverse FFT
e = abs(fftim.ifft2(con))

# e is converted from an ndarray to an imageFourier Transform 125
f = scipy.misc.toimage(e)

# plot
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
