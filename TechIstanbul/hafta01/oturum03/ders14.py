sicaklik = 0

while sicaklik <= 200:
    sicaklik += 50
    match sicaklik:
        case 100:
            print("Dikkat!: Orta sıcaklık ", sicaklik)
            continue
        case 200:
            print("Hazır! ", sicaklik)
            break
    print("fırın sıcaklığı ", sicaklik)