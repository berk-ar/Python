# https://requests.readthedocs.io/en/latest
# https://pypi.org/project/requests 
# pip install requests
# pip list # => kurulmuş olan paketleri görüntüler
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/2') # Tek bir veri geldiği için dict olarak response.json() dict olarak dönüyor.

print(response) # <Response [200]>
print(response.status_code) # 200 -> Başarılı
# Status code: 200 -> OK, 404 = Not Found, 500 = Server Error
print("------------------------------------------------------------------")
print(response.text)    # Gelen verinin text hali
print(type(response.text))  # <class 'str'>
print("------------------------------------------------------------------")
print(response.json())  # JSON verisini dict olarak al
print("------------------------------------------------------------------")
data_json = response.json()
print(type(data_json))  # <class 'dict'>
for data in data_json:
    print(f"{data}:\t{data_json[data]}")