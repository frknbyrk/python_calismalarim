
class otobus:
    def __init__(self,oto_palaka,koltuk_sayı):
        self.oto_plaka=oto_palaka
        self.koltuk_sayı=koltuk_sayı
        self.durum_liste=[0]*self.koltuk_sayı
        self.durum_sözlük={}

    def bilet_sat(self,koltuk_no,cinsiyet,yolcu_adi):
        if self.durum_liste[koltuk_no-1] == 1:
            print(f"{koltuk_no} numaralı koltuk dolu")

        else:
            if (koltuk_no-1) % 2 == 0:
                if  self.durum_liste[koltuk_no] == 1:
                    if cinsiyet == self.durum_sözlük[koltuk_no]["cinsiyet"]:
                        self.durum_sözlük[koltuk_no-1]={"cinsiyet":cinsiyet,"isim":yolcu_adi}
                        self.durum_liste[koltuk_no-1]=1
                    else:
                        print("cinsiyet kural ihlali")
                else:
                    self.durum_sözlük[koltuk_no-1]={"cinsiyet":cinsiyet,"isim":yolcu_adi}
                    self.durum_liste[koltuk_no-1]=1
            else:
                if self.durum_liste[koltuk_no-2] == 1:
                    if cinsiyet == self.durum_sözlük[koltuk_no-2]["cinsiyet"]:
                        self.durum_sözlük[koltuk_no-1]={"cinsiyet":cinsiyet,"isim":yolcu_adi}
                        self.durum_liste[koltuk_no-1]=1
                    else:
                        print("cinsiyet kural ihlali")
                else:
                    self.durum_sözlük[koltuk_no-1]={"cinsiyet":cinsiyet,"isim":yolcu_adi}
                    self.durum_liste[koltuk_no-1]=1

    def bilet_iptal(self,koltuk_no):
        if self.durum_liste[koltuk_no-1] == 1:
            self.durum_liste[koltuk_no-1] = 0
            del self.durum_sözlük[koltuk_no-1]
        else:
            print("o koltuk zaten boş")

    def durum_raporu(self):
        say=0
        for i in self.durum_liste:
            say+=1
            if i == 1:
                print(f"{self.durum_sözlük[say-1]['isim']} ({self.durum_sözlük[say-1]['cinsiyet']})")
            else:
                print(f"{say} nolu koltuk boş")


oto=otobus(69,20)
oto.bilet_sat(1,"E","ahmet")
oto.bilet_sat(2,"K","ayşe")
oto.bilet_sat(2,"E","mehmet")
oto.bilet_sat(3,"k","zeynep")
oto.durum_raporu()

