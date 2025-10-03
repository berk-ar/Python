def en_buyuk_bul(*args):
    max_number = args[0]
    for arg in args:
        if arg > max_number:
            max_number = arg
    return max_number

print(en_buyuk_bul(3,7,5,1,2))  # 7

def en_buyuk_bul2(*args):
    if len(args) == 1:
        return args[0]
    else:
        en_buyuk = en_buyuk_bul2(*args[1:])
        return args[0] if args[0] > en_buyuk else en_buyuk

print(en_buyuk_bul2(3,7,5,1,2))  # 7