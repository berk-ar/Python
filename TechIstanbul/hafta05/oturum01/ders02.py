import requests

# İstek atılacak URL
url = "https://api.github.com"

# GET isteği gönder
response = requests.get(url)

# Gelen yanıtın durum kodunu yazdır
print(f"Durum kodu: {response.status_code}")

if response.status_code == 200:
    print("İstek Başarılı!")
else:
    print("İstek Başarısız. Hata kodu: ", response.status_code)

data = response.json()

for key, value in data.items():
    print(key,":",value)