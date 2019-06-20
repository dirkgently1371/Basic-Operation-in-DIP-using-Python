# Laplacian Edge Detection 

from scipy import ndimage as nd
#from skimage import filters
import matplotlib.pyplot as mpl
from PIL import Image
import numpy as np

img = Image.open('lenna.png').convert('L')

# converting to numpy array
a = np.asanyarray(img)

# performing laplacian filter
#b = filters.laplace(a)
b = nd.filters.laplace(a)

#b.save('meanfilter_lenna.png')

mpl.imshow(b)