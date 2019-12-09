import pandas as pd
import glob

for myfile in glob.glob("*.csv"):
    read_file = pd.read_csv (myfile)
    myfile = myfile.replace('.csv','')
    read_file.to_json (myfile + '.json',orient='records')