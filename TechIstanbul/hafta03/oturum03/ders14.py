# Günlük yazma programı

from datetime import datetime
import os

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
dosyaTxt = bulundugumDizin + "/" + "gunluk.txt"

entry = input("Günlük notunuz: ")
tarih = datetime.now().strftime("%d-%m-%Y %H:%M")

with open(dosyaTxt, "a", encoding="utf-8") as f:
    f.write(f"[{tarih}] {entry}\n")