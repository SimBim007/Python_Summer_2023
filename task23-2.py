import psycopg2
import pandas as pd
con=psycopg2.connect(
    database='postgres',
    user='postgres',
    password='',
    host='127.0.0.1',
    port='5432'
)

cur=con.cursor()#курсор
cur.execute('''SELECT * FROM book ''')
rows=cur.fetchall()
df=pd.DataFrame(rows,columns=[c[0] for c in cur.description])
con.close()
print(df)
