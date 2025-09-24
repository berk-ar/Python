# yöntem 1
"""
cevap = input("pizza ister misiniz?: ")

while cevap.lower() == "evet":
    print("Siparişiniz hazırlanıyor.")
    cevap = input("Bir dilim daha ister misiniz?: ")
"""

# yontem 2

cevap = bool(input("pizza ister misiniz?: "))

while cevap:
    print("Siparişiniz hazırlanıyor.")
    cevap = bool(input("Bir dilim daha ister misiniz?: "))