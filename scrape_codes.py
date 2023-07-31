import requests
from bs4 import BeautifulSoup

url = 'https://www.unitedstateszipcodes.org/in/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

zip_table = soup.find('table', class_='statTable')

ma_zip_codes = []
zips = []

for row in zip_table.find_all('tr')[1:]: 
    zip_code = row.find('td').text.strip()
    ma_zip_codes.append(zip_code)

for code in ma_zip_codes:
    code = code[9:15:1]
    zips.append(code)

print(zips)