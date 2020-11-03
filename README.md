# Amazon-Price-Tracker-App

A Python app that tracks an Amazon product and send you an e-mail when it price falls down.\

It uses some basic web scraping and e-mail sending knowledges.

## How to use

If you wish to use this app :
- Add the url for the product you wish to track here : `URL = 'https://amzn.to/3jV41Tc'`

_It doesn't have to be an Amazon product, but the program might not work with other websites depending on the id values they use for the name and price of their products. So feel free to change the `title` and `price` variables values to match the id used on the website of your choice._


- Replace my user agent with yours here : `headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'}`

_To find your user agent, just google `my user agent` and simply copy the result._


- Replace the server infos with the ones that suit your e-mail account here : `server = smtplib.SMTP('smtp.gmail.com', 587)`

_For example, with an hotmail account you would use `smtplib.SMTP('smtp.live.com', 587)`._


- Replace my server logins info with yours here : `server.login('contact.orlok@gmail.com', 'hbilikxwpkrofbej')`

_The password I used is a generated one with Google App passwords. If you use a gmail address, you can generate one yourself here : `https://bit.ly/2TOr47J`. Otherwise, just use your usual e-mail account password._


- Last but not least for the mailing to work, simply replace my e-mail address with yours here : `server.sendmail('contact.orlok@gmail.com', 'contact.orlok@gmail.com', msg)`

_First line is the sender e-mail address, second one is the recipient e-mail adress._


- The program will check the price of the desired item every 24h, you can change the value (in seconds) to your convenience here : `time.sleep(86400)`

## Executing

Execute the program this way : `python scraper.py`
