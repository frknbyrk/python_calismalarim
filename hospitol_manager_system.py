
class hospitol_manager:
    def __init__(self):
        self.prices={"kardiyoloji": 1000, "dahiliye": 500, "göz": 700}
        self.appointments=[]
    
    def create_appointment(self,patient,doctor,department,date,time):
        say=0
        for i in self.prices:
            if i == department:
                say+=1
        if say == 0:
            print("hatalı bölüm")
            return
        
        time_check=time.split(":")
        if int(time_check[0])<9 or int(time_check[0]) >=17:
            print("mesai saatleri dışı")
            return

        for i in self.appointments:
            if i["date"] == date and i["time"] == time and i["doctor"] == doctor and i["status"] == "aktif":
                print("doktor dolu")
                return

        self.appointments.append({"patient":patient,
                                        "doctor":doctor,
                                        "department":department,
                                        "date":date,
                                        "time":time,
                                        "price":self.prices[department],
                                        "status":"aktif"})
        print(f"randevu onaylandı ücret:{self.prices[department]} TL")        
    
    def cancel_appointment(self,patient,date,time):
        for i in self.appointments:
            if i["patient"] == patient and i["date"] == date and i["time"] == time:
                i["status"] ="iptal"
                i["price"] = 0
                print("randevu iptal edildi")

    def calculate_total_income(self):
        total_income=0
        for i in self.appointments:
            if i["status"] == "aktif":
                total_income += i["price"]
        print(f"toplam tahmini gelir:{total_income} TL")
        
    def save_records(self):
        with open("files/demo.txt","a",encoding="utf-8") as f:   
            for i in self.appointments:      
                f.write(f"hasta adı:{i['patient']} bölüm:{i['department']} durum:{i['status']} ücret:{i['price']}\n")

        

mng=hospitol_manager()

mng.create_appointment("ali","dr.ahmet","nöroloji","12.12.2025","10:00")
mng.create_appointment("ali","dr.ahmet","dahiliye","12.12.2025","19:00")
mng.create_appointment("ali","dr.ahmet","dahiliye","12.12.2025","10:00")
mng.create_appointment("veli","dr.ahmet","dahiliye","12.12.2025","10:00")
mng.create_appointment("ayşe","dr.mehmet","kardiyoloji","12.12.2025","14:00")

mng.calculate_total_income()

mng.cancel_appointment("ali","12.12.2025","10:00")

mng.calculate_total_income()

mng.save_records()



