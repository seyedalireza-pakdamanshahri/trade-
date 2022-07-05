from bs4 import BeautifulSoup
import requests
import time

while True :
    request = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
    a = request.text

    soup = BeautifulSoup(a,"html.parser")
    pretty = soup.prettify()
    c = BeautifulSoup(pretty,"html.parser")

    unchangevalue = c.find("div", class_="priceValue" ).text
    strprice = unchangevalue.replace('$','').replace(' ','').replace("\n","").replace(",","")
    print (strprice)
    file = open("data.text", "a")
    file.write(strprice+"\n")
    file.close
    time.sleep(60)  