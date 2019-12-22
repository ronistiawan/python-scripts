import random
import math

dataku = open("data.txt", "w")

databaru = ""

for x in range(0,100):

    b = str(random.randint(0,101))
    c = str(math.sin(x))
    d = str(math.cos(x))
    e = str(math.tan(x))

    databaru = str(x) + "," + b + "," + c+ "," + d+ "," + e
    dataku.write(databaru)
    dataku.write("\n")
    
dataku.close()
    