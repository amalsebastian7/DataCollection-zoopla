import requests
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/List_of_Real_Madrid_CF_players"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
second_table = soup.find_all('table')[1]
email_addresses = []
for row in second_table.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) >= 4:
        name = columns[0].text.strip()
        years = list(map(int, re.findall(r'\b\d{4}\b', columns[3].text.strip())))
        if any(year >= 2010 for year in years):
            clean_name = name.replace('*', '')
            parts = clean_name.split(' ', 1)
            first_name = parts[0]
            last_name = parts[1] if len(parts) > 1 else ''
            email_addresses.append(first_name.lower() + "@gmail.com")
            if last_name:
                email_addresses.append(last_name.lower().replace(' ', '') + "@gmail.com")

with open('email_addresses.txt', 'w', encoding='utf-8') as file:
    for email in email_addresses:
        file.write(email + '\n')