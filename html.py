import dominate
from dominate.tags import *
import sqlite3
import datetime
from datetime import timedelta
import os

yesterday = datetime.datetime.today() - timedelta(days=1)
yesterday = str(yesterday)
yesterday = yesterday[5:7]+'/'+yesterday[8:10]+'/'+yesterday[2:4]

now = datetime.datetime.now()
fecha = now.strftime('%x')

con = sqlite3.connect('invest.db')
cur = con.cursor()
cur.execute(f'select valor from [AL30 {fecha}]')
AL30=cur.fetchall()
cur.execute(f'select valor from [AL30D {fecha}]')
AL30D=cur.fetchall()
cur.execute(f'select valor from [DAI/ARS {fecha}]')
DAI_ARS=cur.fetchall()
cur.execute(f'select valor from [DAI/USD {fecha}]')
DAI_USD=cur.fetchall()
count=0
lens=[]
lens.append(len(AL30))
lens.append(len(AL30D))
lens.append(len(DAI_ARS))
lens.append(len(DAI_USD))


table_headers=['AL30', 'AL30D', 'DAI/ARS', 'DAI/USD']

def create_page():
    doc = dominate.document(title='Investing Data')

    with doc:
        with div():
            h1('Hello, World!')
            with table():
                with thead():
                    with tr():
                        for table_head in table_headers:
                            th(table_head)
                with tbody():
                    for i in range(min(lens)):
                        with tr():
                            td(AL30[count])
                            td(AL30D[count])
                            td(DAI_ARS[count])
                            td(DAI_USD[count])
    with open('index.html', 'w') as lock:
        lock.write(doc.render())

create_page()
os.system('sudo mv index.html /var/www/html/index.html')