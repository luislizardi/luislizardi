


import requests
from bs4 import BeautifulSoup


#mystocks = ['EPD', 'PZZA', 'XOM', 'SEMR', 'PHYS', 'SILJ', 'DIS', 'PFE', 'COP' ]
stockdata= []

def getData(symbol):

    headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    url= f'https://finance.yahoo.com/quote/{symbol}'

    r=requests.get(url,headers=headers)
#print(r.status_code)
#print(r.text)

    soup=BeautifulSoup(r.text,'lxml')

    try:
        stock= {
        'symbol': symbol,
        'price':soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('span')[0].text,

           'change':soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('span')[1].text
        }

    except:
        print("Ocurrió un error, reintente nuevamente")
        return

    print(stock)
    return stock

while True:
    print()
    symbol = input("Ingrese SIGLAS  de la Compañía según la Bolsa.  9 Para Finalizar:  ")
    print()

    if symbol== "9":
              print()
              print("Proceso Finalizado")
              print()
              break
    else:
        getData(symbol)

    

#    if m_opcion == "9":
#        print(stockdata[8])
        

    





    
