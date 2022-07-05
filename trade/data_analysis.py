from bs4 import BeautifulSoup
import requests
import time
b = 0
while True :
    request = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
    a = request.text

    soup = BeautifulSoup(a,"html.parser")
    pretty = soup.prettify()
    c = BeautifulSoup(pretty,"html.parser")

    unchangevalue = c.find("div", class_="priceValue" ).text
    strprice = unchangevalue.replace('$','').replace(' ','').replace("\n","").replace(",","")
    if b != 0 :
        if float(strprice)/b > 1.008:
            print ("alert green")
        elif float(strprice)/b < 0.991:
            print("alert red")

    file = open("data.text","a")
    price = file.write(strprice)
    file.close
    b = float(strprice)
    print("hello")
    time.sleep(60)