class ogrenciler:

    def __init__(self):
        self.ogrenci_veri={}
        
    def ogrenci_ekle(self,numara,ad,notu):
        if numara in self.ogrenci_veri.keys():
            print("ogrenci var")
        else:
            self.ogrenci_veri[numara]={"isim":ad,"not":notu}
            print("eklendi")

    def ogrenci_sil(self,sil_num):
        if sil_num in self.ogrenci_veri.keys():
            del self.ogrenci_veri[sil_num]
            print("silindi")
        else:
            print("ogrenci yok")

    def not_guncelle(self,gun_num,gun_not):
        if gun_num in self.ogrenci_veri:
            self.ogrenci_veri[gun_num]["not"]=gun_not
        else:
            print("ogrenci yok")

    def ogrenci_ara(self,ara_num):
        if ara_num in self.ogrenci_veri:
            print(f"numara:{ara_num} ad:{self.ogrenci_veri[ara_num]['isim']} not:{self.ogrenci_veri[ara_num]['not']}")
        else:
            print("ogrenci bulunamadı")

    def listele(self):
        if len(self.ogrenci_veri) == 0:
            print("liste bos")
        else:
            for anahtar,deger in self.ogrenci_veri.items():
                print(f"numara:{anahtar}-isim:{deger['isim']}-not:{deger['not']}")

while True:
    islem=int(input())

    if islem == 1:
        num=int(input())
        ad=input()
        notu=int(input())
        ogr=ogrenciler()
        ogr.ogrenci_ekle(num,ad,notu)

    elif islem == 2:
        num=int(input())
        ogr.ogrenci_sil(num)

    elif islem == 3:
        num=int(input())
        notu=int(input())
        ogr.not_guncelle(num,notu)

    elif islem == 4:
        num=int(input())
        ogr.ogrenci_ara(num)

    elif islem == 5:
        ogr.listele()

    elif islem == -1:
        print("cıkıs")
        break

    else:
        print("hata")

