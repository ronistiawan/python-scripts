import pandas as pd
import pandas.io.sql as sqlio
import glob
import psycopg2
import numpy as np

def getConnection():
    return psycopg2.connect(user = "dbuser",
                            password = "dbpassword",
                            host = "dbhost",
                            port = "5433",
                            database = "database_name")

conn = getConnection()

for myfile in glob.glob("*.sql"):
    query = open(myfile,'r').read()

    myfile = myfile.replace('.sql','')
    print(query)
    result = sqlio.read_sql_query(query, conn)


    int_cols = ['dpd_terakhir', 'dpd_max']
    result[int_cols] = result[int_cols].applymap(np.int64)

    result.to_excel("Output/"+myfile + ".xlsx", index = None, header=True)
    result.to_json ("Output/"+myfile + '.json',orient='records')
    result.to_csv("Output/"+myfile + ".csv", sep='|', header=False, index=False)

conn.close()
