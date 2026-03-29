class students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class stuclass12(students):
    pass
student1=stuclass12("vishal",22)
student2=stuclass12("lahsiv",23)
print(student1.name)
print(student2.age)