import base64
import glob

for file in glob.glob("*.png"):
    with open(file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    file = file.replace(".png",".txt")
    textFile = open(file,"w")
    textFile.write(encoded_string.decode('UTF-8'));
    textFile.close()