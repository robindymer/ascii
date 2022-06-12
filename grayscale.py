
import cv2
import numpy as np
import math

# Read and show image
img_grayscale = cv2.imread('testmajd.jpg',0) # 0 = grayscale
# cv2.imshow('graycsale image',img_grayscale)

# scale it
width = 90
height = 60
points = (width, height)
resized = cv2.resize(img_grayscale, points, interpolation = cv2.INTER_LINEAR)

# cv2.imshow('Resized', resized)
# cv2.waitKey()

# cv2.destroyAllWindows() simply destroys all the windows we created.
cv2.destroyAllWindows()
# The function cv2.imwrite() is used to write an image.
cv2.imwrite('grayscale.jpg',img_grayscale)

# Grayscale --> ASCII, cred to http://paulbourke.net/dataformats/asciiart/
chars =  " .:-=+*#%@"
ramp = [c for c in chars]
print(ramp)
def asciiMap(val):
    val_norm = val / 255
    index = math.floor(val_norm/0.101) #0.101 instead of 0.1 to remove 10's
    return index


rows, cols = resized.shape
result = np.empty((rows, cols), dtype='S1')

for i in range(rows):
    for j in range(cols):
        k = resized[i, j]
        index = asciiMap(k)
        result[i, j] = ramp[index]

print(result)

mem = 0
for i in range(rows):
    for j in range(cols):
        if mem != i:
            print('')
            mem = i

        print(result[i, j].decode('utf-8'), end='')
