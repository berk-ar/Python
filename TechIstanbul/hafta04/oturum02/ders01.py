# @property nedir?

# Sınıf içindeki bir metodu, özellik (attribute) gibi kullanmanızı sağlar.
# Yani parantez kullanmadan çağırabiliriz.
# Genellikle okuma, yazma ve silme kontrolü için kullanılır.

class Dikdortgen:
    def __init__(self, en, boy):
        #self.en = en
        self.boy = boy  # public
        
        self._en = en   # private
        #self._boy = boy # private -> (_)

    @property
    def alan(self):
        """Dikdörtgenin alanını döndürür"""
        return self.en * self.boy
    
    @property
    def en(self):
        return self._en
    
    @en.deleter
    def en(self):
        print("En silindi!")
        del self._en
    
dikdortgen1 = Dikdortgen(5, 3)
# print(dikdortgen1.alan())   # TypeError: 'int' object is not callable
print(dikdortgen1.alan) # 15

del dikdortgen1.en