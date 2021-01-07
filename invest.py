import requests
from bs4 import BeautifulSoup

url = 'https://www.invertironline.com/titulo/cotizacion/BCBA/AL30/BONO-REP.-ARGENTINA-USD-STEP-UP-2030/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#AL30
al30page=soup.find_all('span', attrs={'data-field':"UltimoPrecio"})
al30=al30page[0].get_text()
al30=al30.replace('.', '')
al30=al30.replace(',', '.')


print('El bono AL30 está: $', al30)

url = 'https://www.invertironline.com/titulo/cotizacion/BCBA/AL30D/BONO-REP.-ARGENTINA-USD-STEP-UP-2030/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#AL30D
al30dpage=soup.find_all('span', attrs={'data-field':"UltimoPrecio"})
al30d=al30dpage[0].get_text()
al30d=al30d.replace('.', '')
al30d=al30d.replace(',', '.')

usd=float(al30)/float(al30d)

print('El bono AL30D está: u$d', al30d)

print('El valor al que se comprará el dólar es de: $', usd)

url = 'https://criptoya.com/api/buenbit/dai/ars'
page = requests.get(url)

DAI_ARS = page.json()['totalAsk']

url = 'https://criptoya.com/api/buenbit/dai/usd'
page = requests.get(url)

DAI_USD = page.json()['totalAsk']

inversion=usd*200
DAI_comprados=200/DAI_USD
pesosVentaDAI=200/DAI_USD*DAI_ARS
ganancia=pesosVentaDAI-inversion
ganancia_=(pesosVentaDAI*100/inversion)-100

print(f'\nPor el monto de 200 dólares:\nInversión: {inversion}\nDAI comprados: {DAI_comprados}\nPesos obtenidos por la venta de DAI: {pesosVentaDAI}\nGanancia obtenida: {ganancia}\nGanancia porcentual: {ganancia_}\n\nDAI/USD: {DAI_USD}\nDAI/ARS: {DAI_ARS}')