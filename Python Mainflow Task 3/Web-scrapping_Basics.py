import requests
from bs4 import BeautifulSoup



URL = ("https://www.msn.com/en-in/health/health-news/what-happens-to-the-body-if-you-walk-every-day-after-dinner-for"
       "-30-minutes/ar-BB1mZGMP?ocid=msedgntp&pc=U531&cvid=431912d8661c4933a1bf6b2882f6c4c1&ei=6")
r = requests.get(URL)
print(r.content)

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/125.0.0.0 Safari/537.36"}
r = requests.get(url=URL, headers=headers)
print(r.content)



#   Parsing the HTML content
URL = "https://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
