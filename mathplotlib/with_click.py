#Pusat lingkaran ditentukan dengan klik

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import math

image = Image.open('image.jpeg', 'r')   #Membaca gambar
image = image.convert('L')              #convert gambar ke greyscale
data = np.asarray(image)             #konversi gambar ke array

R = 150

def drawCircle(x,y):
    
    global R
    ax.clear()
    ax.imshow(data, cmap='gray')
    circle = patches.Circle((x,y), R, lw=2, ls='-', fill=False, color='red')
    ax.add_patch(circle)
    print("draw circle is called with %d,%d "%(x,y))    
    plt.draw()
    return ax

#----------------------------- * On click event * --------------------------
def onclick(event):
    global xc, yc
    global ax, patches
    total = 0
    n = 0
    xc, yc = event.xdata, event.ydata
    print 'center : (%d,%d)' %(xc, yc) 
    drawCircle(xc,yc)
    #drawCircle(0,0)
    for i in range(0,n_rows):
        for j in range(0, n_columns):
            x = xc - j
            y = yc - i
            r = math.sqrt(x**2+y**2)
            if (r < R+1):
                total += data[i,j]
                n += 1
    
    rata2 = total/n
    print("Rata-rata = %d" %rata2)
    
    #stop listening if user click on top left corner
    if xc < 10 and yc < 10:
        fig.canvas.mpl_disconnect(cid)
        print("stoped listening for events")
#-------------------------------------------------------------------------

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

cid = fig.canvas.mpl_connect('button_press_event', onclick)
print("start listening for mouse clicks ... click on top left corner to stop listening")
plt.show()
plt.draw()
#drawCircle(xc,yc)


