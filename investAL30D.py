import sqlite3
import datetime
import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.invertironline.com/titulo/cotizacion/BCBA/AL30D/BONO-REP.-ARGENTINA-USD-STEP-UP-2030/'
count=0

for i in range(5):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #AL30D
    al30Dpage=soup.find_all('span', attrs={'data-field':"UltimoPrecio"})
    al30D=al30Dpage[0].get_text()
    al30D=al30D.replace('.', '')
    al30D=al30D.replace(',', '.')

    now = datetime.datetime.now()
    fecha = now.strftime('%x')
    hora = now.strftime('%X')
    hora=hora[:5]


    con = sqlite3.connect('invest.db')
    cur = con.cursor()
    cur.execute(f'select id from [AL30D {fecha}] order by id')
    all=cur.fetchall()
    if all==[]:
        last=0
    else:
        last=all[-1]
        last=last[0]
    id=last+1
    entry=(id, hora, al30D)
    cur.execute(f'insert into [AL30D {fecha}](id, hora, valor) values(?, ?, ?)', entry)
    con.commit()
    con.close()
    count+=1
    if count!=5:
        time.sleep(12)