# Amazon-Price-Tracker-App

A Python app that tracks an Amazon product and send you an e-mail when it price falls down.

## How to use

If you wish to use this app :
- Add the url for the product you wish to track here : `URL = 'https://amzn.to/3jV41Tc'`

- Replace my user agent with yours here : `headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'}`
To find your user agent, just google `my user agent` and simply copy the result.

- Replace the server infos with the ones that suit your e-mail account here : `server = smtplib.SMTP('smtp.gmail.com', 587)`
For example, with an hotmail account you would use `smtplib.SMTP('smtp.live.com', 587)`

- Replace my server logins info with yours : `server.login('contact.orlok@gmail.com', 'hbilikxwpkrofbej')`
The password I used is a generated one with Google App passwords. If you use a gmail address, you can generate one yourself here : `https://bit.ly/2TOr47J`. Otherwise, just use your usual e-mail adress account password.

- Last but not least for the mailing to work, simply replace my mail with yours here : `server.sendmail('contact.orlok@gmail.com', 'contact.orlok@gmail.com', msg)`
First line is the sender e-mail, second one is the recipient e-mail adress.

- The program will check the price of the desired item every 24h, you can change the value (in seconds) to your convenience here : `time.sleep(86400)`

## Executing

Execute the program this way : `python scraper.py`
