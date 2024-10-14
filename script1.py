# A script to download the first png image from gsom
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://gsom.spbu.ru/en/')
soup = BeautifulSoup(resp.content, 'html.parser')
images = soup.find_all('img')
pngs = [image for image in images if 'png' in str(image)]
link = pngs[0].attrs['src']

url = 'https://gsom.spbu.ru' + link
response = requests.get(url)
with open('template.png', 'wb') as file:
    file.write(response.content)