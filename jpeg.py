import matplotlib.pyplot as plt
import matplotlib
import numpy as np

from skimage import data
from skimage import color

astronaut = data.astronaut()
plt.figure()
plt.title("astronaut before compression")
plt.imshow(astronaut)
plt.show()


print(astronaut)
print("astronaut shape: {}".format(astronaut.shape))

for dim in range(astronaut.ndim):
    print(astronaut[dim])
    print(astronaut[dim].shape)




def rgb_to_YCbCr(img):
    
    
    Y = 0+(0.299 * img[:,:,0]) + (0.587 * img[:,:,1]) + (0.114 * img[:,:,2])
    Cb = 128 - (0.168736 * img[:,:,0]) - (0.331264 *img[:,:,1]) + (0.5 * img[:,:,2])
    Cr = 128 + (0.5 * img[:,:,0]) - (0.418688 *img[:,:,1]) - (0.081312 * img[:,:,2])
    
    
    return Y, Cb, Cr


def chroma_subsample(Y,Cb,Cr,jab:str):

    if jab == "4:4:2":
        pass
    elif jab == "4:4:1":
        pass






Y, Cb, Cr = rgb_to_YCbCr(astronaut)
jab = [4,4,2]
Y, Cb, Cr = chroma_subsample(Y, Cb, Cr, jab)

