
class course:
    def __init__(self,course_name):
        self.course_name=course_name
        self.teacher_name=None

    def assign_teacher(self,teacher_name):
        self.teacher_name=teacher_name

    def remove_teacher(self):
        self.teacher_name=None

    def get_course_info(self):
        if self.teacher_name == None:
            print(f"Ders adı:{self.course_name} ögretmen henüz atanmamış")
        else:
            print(f"Ders adı:{self.course_name}---Ders öğretmeni:{self.teacher_name}")
    
class teacher_manager:
    def __init__(self):
        self.courses=[]

    def add_courses(self,course_object):
        self.courses.append(course_object)
        print("yeni ders eklendi")
    
    def assign_teacher_to_course(self,course_name,teacher_name):
        for courses in self.courses:
            if courses.course_name == course_name:
                courses.assign_teacher(teacher_name)
                print("öğretmen derse atandı")
                return
        print("ders yok")

    def remove_teacher_from_course(self,course_name):    
        for courses in self.courses:
            if courses.course_name == course_name:
                if courses.teacher_name != None:
                    courses.remove_teacher()
                    print("öğretmen dersten kaldırıldı")
                else:
                    print("derste öğretmen yok")
                return
        print("ders yok")

    def list_courses(self):
        number_of_elements=len(self.courses)
        if number_of_elements !=0:
            for courses in self.courses:
                courses.get_course_info()
        else:
            print("ders listesi boş")

mng=teacher_manager()
ders1=course("mat")
ders2=course("fizik")
ders3=course("programlama")

mng.add_courses(ders1)
mng.add_courses(ders2)
mng.add_courses(ders3)

mng.list_courses()

mng.assign_teacher_to_course("mat","ayşe")
mng.assign_teacher_to_course("fizik","furkan")
mng.assign_teacher_to_course("programlama","şifa")

mng.list_courses()

mng.remove_teacher_from_course("mat")

mng.list_courses()
























"""
key=x.keys()
value=x.values()
item=x.items()

for k in key:
    print(k)
print()

for j in value:
    print(j)
print()

for i in item:
    print(i) 
"""