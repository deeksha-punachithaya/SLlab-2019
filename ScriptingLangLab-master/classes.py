class Person:
	def __init__(self,name,age):
		self.name = name;
		self.age = age;
		
p1 = Person("Deeksha",20)
p2 = Person("Diya",25)

print("Name of person 1 ",p1.name)
print("Name of person 2 ",p2.name)

print("Age of person 1 ",p1.age)

p1.age = 15

print("Age of person 1 ",p1.age)
