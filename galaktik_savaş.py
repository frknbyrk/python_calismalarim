import random
import time

class uzay_gemisi:
    def __init__(self,isim,can,yakıt,saldiri_gucu):
        self.isim=isim
        self.can=can
        self.yakıt=yakıt
        self.saldiri_gucu=saldiri_gucu

    def hasar_al(self,hasar):
        self.can -= hasar
        if self.can < 0:
            self.can = 0
        print(f"{self.isim} isabet aldı {self.can} canı kaldı")

    def ates_et(self,hedef):
        print(f"{self.isim} lazerleri ateşledi")
        hedef.hasar_al(self.saldiri_gucu)


class avci_gemisi(uzay_gemisi):
    def __init__(self,isim,can,yakıt,saldiri_gucu):
        super().__init__(isim,can,yakıt,saldiri_gucu)

    def ates_et(self, hedef):
        yeni_saldırı_gucu=self.saldiri_gucu
        if self.yakıt >= 10:
            self.yakıt -= 10
            yeni_saldırı_gucu=self.saldiri_gucu*2
            print(f"{self.isim} TARAFINDAN TURBO SALDIRI YAPILDI")
        else:
            print("yakıt bitti zayıf atış")
            
        hedef.hasar_al(yeni_saldırı_gucu)

class kruvazor(uzay_gemisi):
    def __init__(self, isim, can, yakıt, saldiri_gucu,kalkan_gucu):
        super().__init__(isim, can, yakıt, saldiri_gucu)
        self.kalkan_gucu=kalkan_gucu

    def hasar_al(self, hasar):
        if self.kalkan_gucu > 0:
            self.kalkan_gucu -= hasar
            if self.kalkan_gucu < 0:
                artan_hasar=abs(self.kalkan_gucu)
                self.kalkan_gucu=0
                print("KALKAN KIRILDI")
                super().hasar_al(artan_hasar)
            else:
                print(f"kalkan hasarı emdi kalan kalkan {self.kalkan_gucu}")
        else:
            super().hasar_al(hasar)

av=avci_gemisi("x-wing",100,30,20)
kr=kruvazor("star destroyer",150,10,15,40)

print("GALAKTİK SAVAŞ BAŞLIYOR")

tur=1
while True:
    print(f"------------{tur}.TUR BAŞLIYOR!!!!------------ ")
    time.sleep(3)

    av.ates_et(kr)

    if kr.can <=0:
        print(f" KAZANAN {av.isim}! İMPARATORLUK GEMİSİ PATLADI")
        break
    print("-"*30)
    time.sleep(3)

    kr.ates_et(av)

    if av.can <= 0:
        print(f"KAZANAN {kr.isim}! ASİLER YOK EDİLDİ")
        break

    print("-"*30)
    tur += 1

    
