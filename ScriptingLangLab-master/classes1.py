class Person:
	def __init__(self,name,age):
		self.name = name;
		self.age = age;
		
p1 = Person("Deeksha",20)

print("Name of person 1 ",p1.name)

del p1.name
#print("Name of person 1",p1.name)

print("Age ",p1.age)

del p1

print("Age",p1.age)


