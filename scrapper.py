import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www2.hm.com/en_in/productpage.0689389048.html'

headers = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0Feedback'}


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('akankshagahlot0307@gmail.com','jafdexyyiqkyqfey')

    subject = 'Price fell down'

    body = 'Check the H&M link https://www2.hm.com/en_in/productpage.0689389048.html'
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'akankshagahlot0307@gmail.com',
        'enraihakazenostigma@gmail.com',
        msg
    )
    print('EMAIL HAS BEEN SENT!')

    server.quit()


def check_price():

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(attrs={"primary product-item-headline"}).get_text()
    price = soup.find(attrs={"price-value"}).get_text()
    pricevalue = price.split()
    priceno = pricevalue[1]
    Rprice = priceno.translate({ord(','): None})
    converted_price = float(Rprice[0:5])

    if(converted_price < 900.0):
        send_mail()

    print(title.strip())
    print(converted_price)

    if(converted_price > 900.0):
        send_mail()

   


while(True):
    check_price()
    time.sleep(3600)