# creating DB connecttion (postgres)

import psycopg2

config={
    'user':'postgres',
    'password':'', # required password
    'host':'localhost',
    'port':'5432'
}

try:
    # passing dic with double **
    conn=psycopg2.connect(**config)
    
    print('Connect to DB')
    
    # get the cursor
    cur=conn.cursor()
    
    print('PostgresSQL database version')

    # create query -- select version of postgres
    cur.execute('SELECT version()')
    
    # fetch result
    db_version=cur.fetchone()
    
    print(db_version)

except:
    print('Unable to connect')

 # connection close
conn.close
