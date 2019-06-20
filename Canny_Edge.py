# Canny Edge Detection 

from skimage import feature
import matplotlib.pyplot as mpl
from PIL import Image
import numpy as np

img = Image.open('lenna.png').convert('L')

# converting to numpy array
a = np.asanyarray(img)

# performing canny filter
b = feature.canny(a,sigma = 1)

#b.save('meanfilter_lenna.png')

mpl.imshow(b)