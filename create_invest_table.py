import sqlite3
import datetime
def sql_connection():
    connection=sqlite3.connect('invest.db')
    return connection

def sql_table(connection, fecha):
    cursor = connection.cursor()
    cursor.execute(f'create table [AL30 {fecha}](id interger PRIMARY KEY, hora text, valor real)')
    cursor.execute(f'create table [AL30D {fecha}](id interger PRIMARY KEY, hora text, valor real)')
    cursor.execute(f'create table [DAI/ARS {fecha}](id interger PRIMARY KEY, hora text, valor real)')
    cursor.execute(f'create table [DAI/USD {fecha}](id interger PRIMARY KEY, hora text, valor real)')
    connection.commit()

now = datetime.datetime.now()
fecha = now.strftime('%x')
fecha = str(fecha)
connection=sql_connection()
sql_table(connection, fecha)