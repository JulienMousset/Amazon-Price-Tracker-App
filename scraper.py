import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.fr/Casque-r%C3%A9alit%C3%A9-virtuelle-Oculus-Rift/dp/B07PTMKYS7/ref=sr_1_1_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=oculus+rift&qid=1604399079&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRUNFWDk5M1dFMDBaJmVuY3J5cHRlZElkPUEwNDg0MzczMlQyRFNGMjBSSUkwWCZlbmNyeXB0ZWRBZElkPUEwMjY5OTU5MjY3NldYSFNUS0NVOCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])

    print(converted_price)
    print(title.strip())
    
    if(converted_price > 400.0):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('contact.orlok@gmail.com', 'hbilikxwpkrofbej')

    subject = 'Oculus Rift price fell down'
    body = 'Check it out:\nhttps://www.amazon.fr/Casque-r%C3%A9alit%C3%A9-virtuelle-Oculus-Rift/dp/B07PTMKYS7/ref=sr_1_1_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=oculus+rift&qid=1604399079&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRUNFWDk5M1dFMDBaJmVuY3J5cHRlZElkPUEwNDg0MzczMlQyRFNGMjBSSUkwWCZlbmNyeXB0ZWRBZElkPUEwMjY5OTU5MjY3NldYSFNUS0NVOCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

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