gun = int(input("Haftanın kaçıncı günü: "))

match gun:
    case 1:
        print("Pazartesi")
    case 2:
        print("Salı")
    case 3:
        print("Çarşamba")
    case 4:
        print("Perşembe")
    case 5:
        print("Cuma")
    case 6:
        print("Cumartesi")
    case 7:
        print("Pazar")
    case _:
        print("Hatalı gün girişi")

match gun:
    case 1 | 3 | 6:
        print("Bugün Python Bootcamp Var")
    case 2 | 4 | 5 | 7:
        print("Bootcamp yok.")
    case _:
        print("Hatalı gün girişi")