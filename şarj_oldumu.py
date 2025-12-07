
class telefon:
    def __init__(self,model,sarj_yuzdesi):
        self.model=model
        self.sarj_yuzdesi=sarj_yuzdesi

    def sarj_ol(self,miktar):
        self.sarj_yuzdesi+=miktar
        if self.sarj_yuzdesi > 100:
            self.sarj_yuzdesi = 100
        print(f"telefon şarj oldu,mevcut yuzde:{self.sarj_yuzdesi}")
    def kontrol(self):
        if self.sarj_yuzdesi == 100:
            return 1
        else:
            return 0

class sarj_aleti:
    def __init__(self,guc):
        self.guc=guc
        
    def telefona_tak(self,telefon_nesnesi):
        telefon_nesnesi.sarj_ol(self.guc)

tel=telefon("redmi",10)
sarj=sarj_aleti(20)
say=0
while True:
    say+=1
    sarj.telefona_tak(tel)
    x=tel.kontrol()

    if x == 1:
        print("şarjınız dolmuştur")
        break
    print(say)