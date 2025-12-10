class urun:
    def __init__(self,fiyat,urun_id):
        self.fiyat=fiyat
        self.urun_id=urun_id
        print(f"ürünün id:{self.urun_id}--ürünün fiyatı:{self.fiyat}")

class telefon(urun):
    def __init__(self,fiyat,urun_id,kamera_mp):
        super().__init__(fiyat,urun_id)
        self.kamera_mp=kamera_mp

class bilgisayar(urun):
    def __init__(self,fiyat,urun_id,ram_kapasitesi):
        super().__init__(fiyat,urun_id)
        self.ram_kapasitesi=ram_kapasitesi



class magaza:
    def __init__(self,magazanın_adı):
        self.magaza_adı=magazanın_adı
        self.urunler=[]
        self.stoklar={}      

    def urun_ekle(self,urun_nesnesi,stok_adedi):
        self.urunler.append(urun_nesnesi)
        self.stoklar[urun_nesnesi.urun_id] = stok_adedi
    
    def stok_konrol(self,urun_id):
        if urun_id in self.stoklar.keys():
            print(f"{urun_id} id numaralı üründen {self.stoklar[urun_id]} adet var")
        else:
            print("ürün bulunamadı")

class musteri:
    def __init__(self,ad,bakiye):
        self.ad=ad
        self.bakiye=bakiye
        self.sepet=[]
    
    def sepete_ekle(self,urun_nesnesi,magaza_nesnesi):
        if magaza_nesnesi.stoklar[urun_nesnesi.urun_id] > 0:
            self.sepet.append(urun_nesnesi)
            magaza_nesnesi.stoklar[urun_nesnesi.urun_id]-=1
            print("sepete eklendi")
        else:
            print("stok tükenmiş")

    def satin_al(self,magaza_nesnesi):
        toplam_tutar=0
        for urunler in self.sepet:
            toplam_tutar +=urunler.fiyat

        if self.bakiye >= toplam_tutar:
            self.bakiye -= toplam_tutar
            self.sepet=[]
            print(f"alışveriş tamamlandı kalan bakiye {self.bakiye}")

        else:
            print("bakiye yetersiz ürünleri iade ediyorum")
            for urun in self.sepet:
                magaza_nesnesi.stoklar[urun.urun_id]+=1



mgz=magaza("teknostore")
tel=telefon(5000,"T1",64)
blg=bilgisayar(10000,"B1",16)
must=musteri("ali",20000)

mgz.urun_ekle(blg,1)
mgz.urun_ekle(tel,3)
must.sepete_ekle(blg,mgz)
must.sepete_ekle(tel,mgz)
must.sepete_ekle(blg,mgz)
must.satin_al(mgz)
