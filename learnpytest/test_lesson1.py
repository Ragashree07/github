class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"The name is {self.name}")
a=A("sona",23)
a.show()