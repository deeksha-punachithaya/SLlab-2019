class Student:
	def __init__(self,name,age,marks):
		self.name = name
		self.age = age
		self.marks = marks
	def disp(self):
		print("Name " + self.name)
		print("Age " + str(self.age))
		print("Marks ",self.marks)
	def accept(self):
		self.name = input('Enter name of person ')
		self.age = input('Enter age ')
	def listaccept(self):
		marks_str = input('Please enter marks of three subjects as a space-separated string ')
		self.marks = marks_str.split()
		
s1 = Student("Deeksha",20,[50,67,80]);
s1.disp();
s2 = Student("ABC",12,[34,55,66]);
s1.disp();
s1.accept()
s1.listaccept()
s1.disp()
s2.accept()
s2.listaccept()
s2.disp()



