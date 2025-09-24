carpim = 1
while True:
  sayi = int(input("Sayı giriniz: "))
  if not(sayi == 0):
    carpim *= sayi
    print(carpim)
  else:
    print("Girdiğiniz sayıların çarpımı: ",carpim)
    break
  