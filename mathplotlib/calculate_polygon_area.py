from PIL import Image
import numpy as np
from matplotlib.path import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

image = Image.open('samp3.png', 'r')    #read image
image = image.convert('L')              #convert image to greyscale
data = np.asarray(image)                #convert image to numpy array
n_rows = len(data)
n_columns = len(data[0])

point = []

#-------------------------- * Draw Point *-------------------------
def drawCircle(x,y):
    global ax
    circle = patches.Circle((x,y), 2, lw=1, ls='-', fill=True, color='red')
    ax.add_patch(circle)
    plt.draw()
    return ax

#-------------------------- * Draw Polygon and calculate average of pixel values *------
def drawPolygon(p):
    global point
    line = patches.Polygon(point, lw=1, ls='-', fill=False, color='red')
    ax.add_line(line)
    plt.draw()
    
    p = Path(point)
    
    total = 0
    n = 0
    
    for i in range(0,n_rows):
        for j in range(0, n_columns): 
            if(p.contains_point([i,j])):
                total += data[i][j]
                n += 1
    
    print("Average pixel values in the Polygon = "+ str(total/n))
    

#----------------------------- * On click event * --------------------------
def onclick(event):
    global xc, yc
    global ax, patches
    global point
    
    x, y = event.xdata, event.ydata
        
    #stop listening if user click on top left corner
    if event.dblclick:
        drawPolygon(point)
        fig.canvas.mpl_disconnect(cid)
        #print("stoped listening for events")
        
    else:
        point.append([x,y])
        print 'added vertice : (%d,%d)' %(x, y)
        drawCircle(x,y)
    
    return point
#-------------------------------------------------------------------------

fig,ax = plt.subplots(1)
ax.imshow(data, cmap='gray')

cid = fig.canvas.mpl_connect('button_press_event', onclick)
print("start listening for mouse clicks ... click on top left corner to stop listening")
plt.show()
plt.draw()