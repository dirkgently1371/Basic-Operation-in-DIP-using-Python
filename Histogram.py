## Histogram Equalization
import numpy as np
from scipy.misc.pilutil import Image
import scipy.misc
import matplotlib.pyplot as plt

# Reading Image
img = Image.open('lenna.png').convert('L')
# Converting to n dimantional array
img1 = scipy.misc.fromimage(img)
# Converting to 1 dimentional matrix
fl = img1.flatten()
# Histogram and bins computation
hist,bins = np.histogram(img1,256,[0,255])
# CDF Computing
cdf = hist.cumsum()
# Eliminating zerosvof cdf 
cdf_m = np.ma.masked_equal(cdf,0)
# Histogram equalization
num_cdf_m = (cdf_m - cdf_m.min())*255
den_cdf_m = (cdf_m.max()-cdf_m.min())
cdf_m = num_cdf_m/den_cdf_m
# adding 0 into the masked places in cdf_m 
cdf = np.ma.filled(cdf_m,0).astype('uint8')
# cdf values are assigned in the flattened array
img2 = cdf[fl]
# im2 is 1D so we use reshape command to make it into 2D
img3 = np.reshape(img2,img1.shape)
# converting ndarray to image
img4 = scipy.misc.toimage(img3)
# saving result
#img4.save('HE of lenna.png')

# make new figure with 2 subfigures each subfigure can have an image in it
fig = plt.figure()
image1 = plt.subplot(121)
image2 = plt.subplot(122)

# put the images into the window
_ = image1.imshow(img)
_ = image2.imshow(img4)

# hide axis and show window with images
image1.axis("on")
image2.axis("on")
plt.show()
