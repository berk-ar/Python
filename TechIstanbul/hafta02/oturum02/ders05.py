urunler = [
    {
        "urun": "laptop",
        "fiyat": 10000,
        "stok": 20
    },
    {
        "urun": "klavye",
        "fiyat": 5000,
        "stok": 10
    },
    {
        "urun": "kulaklık",
        "fiyat": 1000,
        "stok": 5
    }
]

for urun in urunler:
    print(urun)
    print(f"{urun["urun"]} - {urun["fiyat"]} - {urun["stok"]}")