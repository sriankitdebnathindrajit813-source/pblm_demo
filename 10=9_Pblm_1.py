class Students:
    __student_name = "Abul Kalam"    
    student_role = 25

    def get_student_name(self):
        return self.__student_name

class Students:
    def __init__(self, name, roll=None):
        self.__name = name
        self.__roll = roll

    def get_name(self):
        return self.__name
    
    def get_roll(self):
        return self.__roll
    
    def update_roll(self, update_role):
        self.__roll = update_role

    def get(self):
        data = {
            "name": self.__name,
            "roll": self.__roll
        }
        return data

st = Students(name="Tamim", roll=34)
st2 = Students("Hamim")
st2.update_roll(update_role=2)

print("Name  ----    Role")
for item in [st, st2]:
     # print(f"{item.get_name()} --- {item.get_roll()}")
     print(item.get())