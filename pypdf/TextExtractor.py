import PyPDF2 as pp
import re

#insert the pdf filename where data extracted from
filename = ["57","56"]
#filename = ["47","48","49","50","51","52","53","54","55","56","57","58","66","67","90","91","92"]
#sample 65 sp=2

for a in filename:
    sp = 2 #index of page which Line starts
    n=sp
    
    file = pp.PdfFileReader(str(a)+".pdf", "rb")
    N = file.getNumPages()
    
    textfile = open(str(a)+"-cleaned.txt","w") 
    c = []
    
    while n<N:
        page = file.getPage(n)
        data = page.extractText()
        
        allName = re.findall("CompName:[^\n]{0,200}",data)
        #print("Line#"+str(n-sp+1))
        textfile.write("Line#"+str(n-sp+1)+"\n")
             
        hit = 1
        for i in allName:
            name = i.replace("CompName:","")
            if not c.__contains__(name.lower()):
                c.append(name.lower())
                textfile.write("hit#"+str(hit)+": "+name+"\n")
            hit+=1
        n+=1
    textfile.close()
