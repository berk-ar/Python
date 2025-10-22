import requests

try:
    # İstek atılacak URL
    url = "https://jsonplaceholder.typicode.com/users/1"

    # GET isteği gönder
    response = requests.get(url)

    if response.status_code == 200:
        print("İstek Başarılı!")
        user_data = response.json()

        # Sözlük üzerinden verilere eriş
        print(f"Kullanıcı adı: {user_data['name']}")
        print(f"E-posta: {user_data['email']}")

        # İç içe geçmiş verilere erişim (address bir sözlük)
        print(f"Şehir: {user_data['address']['city']}")
    else:
        print("İstek Başarısız. Hata kodu: ", response.status_code)
except Exception as e:
    print("Yaşanan hata:", e)