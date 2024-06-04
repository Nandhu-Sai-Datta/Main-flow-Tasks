from bs4 import BeautifulSoup
import re
import csv
import requests

url = "https://www.values.com/inspirational-quotes"
r = requests.get(url)
bs = BeautifulSoup(r.content, 'html5lib')
images = bs.find_all('img', {'src': re.compile('.png')})
headings = bs.find_all('h5')
with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    for i in range(len(images)):
        image = images[i]['src']

        print(",", image)
        writer.writerow([image])

    for j in range(len(headings)):
        print(headings[j])
        writer.writerow([image])
