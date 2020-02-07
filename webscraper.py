from bs4 import BeautifulSoup
import requests

url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
yields = content.find("td", attrs={"class": "text_view_data"}).text

for yields in content.findAll("td", attrs={"class": "text_view_data"}):
    print(yields.text.encode('utf-8'))

print(yields)
