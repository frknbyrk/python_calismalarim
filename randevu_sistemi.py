class appointment_system:
    def __init__(self):
        self.appointments=[]

    def add_appointment(self,patient,doctor,date,time):
        for i in self.appointments:
            if i["doktor"].lower() == doctor.lower() and i["tarih"] == date and i["saat"] == time:
                print("bu randevu dolu")
                return
        self.appointments.append({"hasta":patient,"doktor":doctor,"tarih":date,"saat":time})
        print(f"hasta:{patient}--doktor:{doctor}--tarih:{date}--saat:{time}")
        print("randevu oluşturuldu")

    def cancel_appointment(self,patient,date,time):
        for i in self.appointments:
            if i["hasta"] == patient and i["tarih"] == date and i["saat"] == time:
                self.appointments.remove(i)
                print("randevu silindi")
                return
        print("randevu bulunamadı")

    def list_doctor_schedule(self,doktor):
        say=0
        for i in self.appointments:
            if i["doktor"] == doktor:
                print(f"{i["doktor"]} beyin randevuları")
                print(f"hasta:{i['hasta']}--tarih:{i['tarih']}--saat:{i['saat']}")
                say+=1
        if say == 0:
            print("doktorun hiç randevusu yok")

    def list_appointments(self):
        if len(self.appointments) == 0:
            print("randevu bulunmamaktadır")
        for i in self.appointments:
            print(f"hasta:{i['hasta']}--doktor:{i['doktor']}--tarih:{i['tarih']}--saat:{i['saat']}")


appo=appointment_system()   

appo.add_appointment("ali yılmaz","dr.ahmet","12.12.2025","09:00")
appo.add_appointment("ayşe demir","dr.mehmet","12.12.2025","10:00")
appo.add_appointment("veli can","dr.ahmet","12.12.2025","09:00")

appo.list_doctor_schedule("dr.ahmet")

appo.cancel_appointment("ali yılmaz","12.12.2025","09:00")

appo.list_appointments()
