import sqlite3
import datetime
import requests
from bs4 import BeautifulSoup
import time

url = 'https://criptoya.com/api/buenbit/dai/usd'
count=0

for i in range(5):
    page = requests.get(url).json()

    #AL30
    DAI_USD=page['totalAsk']

    now = datetime.datetime.now()
    fecha = now.strftime('%x')
    hora = now.strftime('%X')
    hora=hora[:5]


    con = sqlite3.connect('invest.db')
    cur = con.cursor()
    cur.execute(f'select id from [DAI/USD {fecha}] order by id')
    all=cur.fetchall()
    if all==[]:
        last=0
    else:
        last=all[-1]
        last=last[0]
    id=last+1
    entry=(id, hora, DAI_USD)
    cur.execute(f'insert into [DAI/USD {fecha}](id, hora, valor) values(?, ?, ?)', entry)
    con.commit()
    con.close()
    count+=1
    if count!=5:
        time.sleep(12)