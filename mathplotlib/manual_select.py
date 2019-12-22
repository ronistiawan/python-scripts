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
        if(data[i][j] > 115):
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
R = math.sqrt(dx**2+dy**2)


circle = patches.Circle((xc,yc), R, lw=2, ls='-', fill=False, color='red')
ax.add_patch(circle)

#--------------------------* Menghitung rata-rata *---------------------------
point = []
total = 0
n = 0

for i in range(0,n_rows):
    for j in range(0, n_columns):
        x = xc - j
        y = yc - i
        r = math.sqrt(x**2+y**2)
        if (r < R+1):
            #point.append([i,j])
            total += data[i,j]
            n += 1

#example = [[10,100],[200,20]]
#line = patches.Polygon(point, lw=1, ls='-', fill=False, color='red')
#plt.gca().add_line(line)

rata2 = total/n
print(rata2)