class Student:
    def __init__(self, name, lastName, birthDate, mobile, gender):
        self.name = name
        self.lastName = lastName
        self.birthDate = birthDate
        self.mobile = mobile
        self.gender = gender
        
        print(f" {self.name} {self.lastName} birth in {self.birthDate} and his number is {self.mobile} and gender is {self.gender} ")

student_1 = Student("sina", "omrani", "2014/03/03", "00989122322222", "male")




