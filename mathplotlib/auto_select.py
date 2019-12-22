import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import math

image = Image.open('image.jpeg', 'r')   #Membaca gambar
image = image.convert('L')              #convert gambar ke greyscale
data = np.asarray(image)             #konversi gambar ke array

fig,ax = plt.subplots(1)
ax.imshow(data, cmap='gray')

n_rows = len(data)
n_columns = len(data[0])

left = []
top = []

for i in range(0,n_rows):
    for j in range(0, n_columns): 
        if(data[i][j] > 120):
            top.append(i)
            left.append(j)

xmin = np.min(left)
xmax = np.max(left)

ymin = np.min(top)
ymax = np.max(top)

dx = (xmax-xmin)/2
dy = (ymax-ymin)/2

xc = xmin + dx
yc = ymin + dy
r = math.sqrt(dx**2+dy**2)

#Circle
circle = patches.Circle((xc,yc), r, lw=2, ls='-', fill=False, color='red')
ax.add_patch(circle)

#==================================== Menyimpan data setiap pixel di file txt
#==================================== CARA 2 (LEBIH SIMPEL)
np.savetxt("data numpy.txt", data, fmt="%d", delimiter=",")