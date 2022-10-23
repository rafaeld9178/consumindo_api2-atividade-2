import requests, json
import sqlite3

con = sqlite3.connect("cotacoes.db")
cur = con.cursor()

request = requests.get("https://api.hgbrasil.com/finance?format=json/quotations?key=665616e3")
data = json.loads(request.content)

dolar = data['results']['currencies']['USD']['buy']
euro = data['results']['currencies']['EUR']['buy']

real = float(input('Digite o valor em reais:'))

conversao_dolar = real*dolar
conversao_euro = real*euro

cur.execute("""
    INSERT INTO Cotacao ('Dolar', 'Euro', 'data') VALUES
        (?,?,DATE('now'))""", (dolar, euro))
con.commit()

print("O valor de", real, "reais convertido é:")
print(conversao_dolar, "dólares")
print(conversao_euro, "euros")


