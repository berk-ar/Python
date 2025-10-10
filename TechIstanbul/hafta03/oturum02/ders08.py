import json

# Python objesini JSON string'e çevirme
data = {"isim": "Berk", "yas": 25, "mevki": ["Forvet", "Sol Kanat"]}
jsonStr = json.dumps(data, ensure_ascii = False, indent = 2)
print(jsonStr, type(jsonStr))   # <class 'str'>

# JSON string'ini Python objesine çevirme
parsed = json.loads(jsonStr)
print(type(parsed)) # <class 'dict'>
print(parsed["isim"])   # Berk

# Dosyaya JSON yazma
"""
with open("hafta03/oturum02/veri.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii= False, indent= 2)
"""

# JSON dosyasını okuma
"""
with open("hafta03/oturum02/veri.json", "r", encoding="utf-8") as f:
    okuma = json.load(f)
    print(okuma)
"""