import requests
from bs4 import BeautifulSoup

#####################  SECCION DE SCRAPIN  ####################

print(":::::::::::  El Universal  :::::::::::::::::::::::::")
print("::::::::::::: Titulares y enlaces ::::::::::::::::::::::::::")
print("")
url = "https://www.eluniversal.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")
#print (soup.prettify())
#print (titulos)
#titulos = soup.find_all ("h1"-title")
content_title = soup.find_all("div","col-xs-4")

for tit in content_title:
    sub=tit.find_all("a")
    print(sub[0].attrs.get("title"))
    print(sub[0].attrs.get('href'))
    
    print(" ")
    

##


