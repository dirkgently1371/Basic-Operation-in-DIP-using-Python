## Log Transform

import scipy.misc
import matplotlib.pyplot as plt
from scipy.misc.pilutil import Image
import numpy

# opening the image and converting it to grayscale
a = Image.open('lenna.png').convert('L')

# a is converted to an ndarray
b = scipy.misc.fromimage(a)

# gamma is initialized
gamma1 = .5
gamma2 = 4

# b is converted to type float
b1 = b.astype(float)

# maximum value in b1 is determined
b2 = numpy.max(b1)

# Log transform is computed
c = (255.0*numpy.log(1+b1))/numpy.log(1+b2)

# c is converted to type int
c1 = c.astype(int)

# c1 is converted from ndarray to image
d1= scipy.misc.toimage(c1)

# make new figure with 2 subfigures each subfigure can have an image in it
fig = plt.figure()
image1 = plt.subplot(121)
image2 = plt.subplot(122)

#put the images into the window
_ = image1.imshow(a)
_ = image2.imshow(d1)

#hide axis and show window with images
image1.axis("on")
image2.axis("on")
plt.show()
