import pandas as pd
import glob
import pyodbc
import numpy as np

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8CL7LAT\SQLEXPRESS;DATABASE=DB_NAME;UID=userId;PWD=userPassword')

for myfile in glob.glob("*.sql"):
    query = open(myfile,'r').read()
    myfile = myfile.replace('.sql','')
    print(query)
    result = pd.read_sql_query(query, cnxn)

    # Uncomment these lines to format specific columns
    # int_cols = ['dpd_terakhir', 'dpd_max']
    # result[int_cols] = result[int_cols].applymap(np.int64)

    result.to_excel("Output/"+myfile + ".xlsx", index = None, header=True)
    result.to_json ("Output/"+myfile + '.json',orient='records')
    result.to_csv("Output/"+myfile + ".csv", sep='|', header=False, index=False)

cnxn.close()