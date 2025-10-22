from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# https://pypi.org/project/SQLAlchemy

engine = create_engine('sqlite:///C:/PythonEdu/Python/TechIstanbul/hafta04/oturum03/kutuphane_orm.db')

Base = declarative_base()

Session = sessionmaker(bind = engine)
session = Session()

class Kitap(Base):
    __tablename__ = "kitaplar" # veri tabanında oluşturulacak tablonun adı

    id = Column(Integer, primary_key= True)
    ad = Column(String)
    yazar = Column(String)

    def __repr__(self):
        return f"Kitap (id={self.id}, ad={self.ad}, yazar={self.yazar})"

Base.metadata.create_all(engine)

# kitap1 = Kitap(ad= "Python Dersleri", yazar= "Berk AR")
# session.add(kitap1)

kitap2 = Kitap(ad= "Kotlin Dersleri", yazar= "Berk AR")
# kitap3 = Kitap(ad= "Muhasebe Dersleri", yazar= "Tuğba AR")

session.add_all([kitap2])
session.commit()

tum_kitaplar = session.query(Kitap).all()
print(type(tum_kitaplar))   # <class 'list'>
print(tum_kitaplar) # [Kitap (id=1, ad=Python Dersleri, yazar=Berk AR), Kitap (id=2, ad=Kotlin Dersleri, yazar=Berk AR), Kitap (id=3, ad=Muhasebe Dersleri, yazar=Tuğba AR)]

for i in tum_kitaplar:
    print(i)

print("----------------------------------------------")

guncellenecek_kitap = session.query(Kitap).filter(Kitap.id == 1).first()
guncellenecek_kitap.ad = "Python Bootcamp Dersleri"
session.commit()

for i in tum_kitaplar:
    print(i)

print("----------------------------------------------")

silinecek_kitap = session.query(Kitap).filter(Kitap.ad == "Kotlin Dersleri").first()
sonuc = session.delete(silinecek_kitap)
print(sonuc)
session.commit()

tum_kitaplar2 = session.query(Kitap).all()
for i in tum_kitaplar2:
    print(i)