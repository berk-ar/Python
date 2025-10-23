import requests
from bs4 import BeautifulSoup

url = "https://google.com"

response = requests.get(url)

print("Status code:",response.status_code)  # Status code: 200

# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

print("Sitenin başlığı:",soup.title.text)   # Sitenin başlığı: Google
print("Sitenin scrpit'i:",soup.script.text) # Sitenin script'i => Bütün script kodlarını yazdırır