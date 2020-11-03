import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://amzn.to/3jV41Tc'
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])

    print(title.strip() + ': ')
    print(converted_price)
    if(converted_price < 400.0):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('contact.orlok@gmail.com', 'hbilikxwpkrofbej')

    subject = 'Amazon Price Tracker App : Your item price fell down !'
    body = 'Check it out here :\n' + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'contact.orlok@gmail.com',
        'contact.orlok@gmail.com',
        msg
    )
    print('AN EMAIL HAS BEEN SENT!')
    server.quit()

while(True):
    check_price()
    time.sleep(86400)