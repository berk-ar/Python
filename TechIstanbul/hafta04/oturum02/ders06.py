# Python'da kapsülleme, katı kurallar yerine
# iyi niyetli programlama konvansiyonlarına dayanır.
# Erişim belirteçleri, kodunuzun neresinin "iç işleyiş" ve neresinin "dış arayüz" olduğunu belirtmenizi sağlar.
# yönetilebilir kod yazmanın temelidir.

class Sporcu():
    def __init__(self, ad, brans, altin, gumus, bronz):
        self.ad = ad
        self.brans = brans
        self.mbronz = bronz     # public halka açık değişken
        self._mgumus = gumus    # protected yani yarı gizli
        self.__maltin = altin   # private tam gizli
    def atletBilgisi(self):
        return f"Sporcu adı {self.ad}, branşı: {self.brans}"
    @property
    def a_yazdir(self):
        amadalya = self.__maltin
        return f"altın madalya sayısı: {self.__maltin}"
    
futbolcu1 = Sporcu("Berk", "Futbol", 5,3,1)
print(futbolcu1.atletBilgisi()) # Sporcu adı Berk, branşı: Futbol
print("Bronz madalya sayısı: ",futbolcu1.mbronz)
print("Gümüş madalya sayısı: ",futbolcu1._mgumus)
# print("Altın madalya sayısı: ",futbolcu1.__maltin)  # AttributeError: 'Sporcu' object has no attribute '__maltin'
print(futbolcu1.a_yazdir)   # altın madalya sayısı: 5 # => @property olduğu için private __maltin attribute erişebildik.