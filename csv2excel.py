import pandas as pd
import glob

for myfile in glob.glob("*.csv"):
    read_file = pd.read_csv (myfile,low_memory=False)
    myfile = myfile.replace('.csv','')
    read_file.to_excel (myfile + '.xlsx', index = None, header=True)