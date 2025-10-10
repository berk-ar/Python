import random

print(random.randint(1,5))  # 1 ile 5 arasında bir rastgele sayı üretir
print(random.choice(["maça","kupa","karo","as"]))

renk = '#'
for i in range(6):
    renk = renk + random.choice('ABCDEF1234567890')
print(renk) # Rastgele renk üretir

# from random import randint -> random kütüphanesinden sadece randint getirir.