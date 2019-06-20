## Gamma Correction

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
b3 = numpy.max(b1)

# b1 is normalized
b2 = b1/b3

# gamma-correction exponent is computed
b3 = numpy.log(b2)*gamma1
b4 = numpy.log(b2)*gamma2

# gamma-correction is performed
c1 = numpy.exp(b3)*255.0
c2 = numpy.exp(b4)*255.0

# c is converted to type int
c1 = c1.astype(int)
c2 = c2.astype(int)

# c1 is converted from ndarray to image
d1 = scipy.misc.toimage(c1)
d2 = scipy.misc.toimage(c2)

# displaying the images
f = plt.figure()
f.add_subplot(1,2, 1)
plt.imshow(d1)
f.add_subplot(1,2, 2)
plt.imshow(d2)
plt.show(block=True)
