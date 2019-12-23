#!/usr/bin/env python
# coding: utf-8

# ### Atomic elements

# In[2]:


dict = {'H':'Hydrogen', 'He':'Helium', 'Be':'Beryllium', 'Li':'Lithium'}
dict['B'] = 'Boron'


# In[6]:


for i in dict:
    print("Key is: ",i,"Element is: ",dict[i])


# In[9]:


numb = len(dict)
print("Original number of elements is: ", numb)


# In[10]:


"enter new atomic symbol"


# In[11]:


answer = "y"
while answer == "y":
    key = input('Enter symbol')
    value = input('Name')
    dict[key] = value
    answer = input('Do you want to enter more elements?')


# In[12]:


print(dict)


# In[13]:


len(dict)


# In[16]:


search = input('Search')


# In[17]:


if search in dict:
    print('Exists')
    print('Its value is: %s' %dict[search])
else:
    print('Doesnt exist')


# In[ ]:


#strs = ['ccc', 'aaaa', 'd', 'bb']
#  print sorted(strs, key=len)  ## ['d', 'bb', 'ccc', 'aaaa']


# ### File Handling

# In[30]:


escape = open('Escape.txt')

dic = {}
for line in escape:
    print(line)
    myline = line.split()
    print(myline)
    for word in myline:
        w = dic.get(word,0) + 1
        dic[word] = w
print(dic)

search =input("Enter search string: ")
if search in dic: 
    print("Found word %s %d times" %(search, dic[search]))
else: 
    print ("Sorry! Not found")


# In[31]:


count=0
for k in sorted(dic, key=dic.get, reverse = True):
    print(k, dic[k])
    count = count + 1 
    if count>=10:
        break


# In[37]:


dict = list(dic.values())
dict


# In[34]:


import functools
import statistics


# In[42]:


import operator
sum = (functools.reduce(operator.add,dict))
sum


# In[43]:


print(sum/len(dict))


# In[45]:


list1 = [x*x for x in range(0,15) if x%2 != 0]
list1


# ### Temperature Converter

# In[46]:


c2f = lambda c : (c*9/5)+32
c2k = lambda c : (c+273.15)
f2c = lambda f : (f-32)*5/9
f2k = lambda f : (f2c(f)+273.15)
k2c = lambda k : (k-273.15)
k2f = lambda k : (c2f(k-273.15))
# method to select conversion functions based on units passed
method = lambda fromTemp, toTemp ,temp : globals()[fromTemp+"2"+toTemp](temp)
# to hold conversion
conv = list()
# list driven program
while True:
    x=input("Enter\n1 - Convert Temperature\n2 - Show Conversions\n3 - Exit\nResponse: ")
    if x=='1' :
        fromTemp=input("Enter Original Unit (k/c/f): ").lower()
        toTemp=input("Enter New Unit (k/c/f): ").lower()
        if fromTemp in ['k', 'c', 'f'] and toTemp in ['k', 'c', 'f'] and fromTemp!=toTemp :
            temp=float(input("Enter Temperature: "))
            convTemp=round(method(fromTemp, toTemp, temp),2)
            print(temp, fromTemp, "-->", convTemp, toTemp)
            conv.append((str(temp)+fromTemp, str(convTemp)+toTemp))
        else:
            print("Invalid Input")
    elif x=='2' :
        for i in conv:
            print(i[0]+" --> "+i[1])
    elif x=='3' :
        break
    else:
        print("Invalid Input")


# ### Student Class

# In[47]:


class Student:
    def __init__(self, name=None, age=None, p=None, c=None, m=None):
        self.name=name
        self.age=age
        self.mark=[p,c,m]
    def accept(self):
        self.name=input("Name: ")
        self.age=input("Age: ")
        self.mark=[int(input("Physics Marks: ")), int(input("Chemistry Marks: ")), int(input("Mathematics Marks: "))]
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Physics Marks:",self.mark[0])
        print("Chemistry Marks:",self.mark[1])
        print("Mathematics Marks:",self.mark[2])

std1=Student()
std2=Student()
print("*"*25,"\nEnter Data")
std1.accept()
print("-"*25)
std1.display()
print("*"*25,"\nEnter Data")
std2.accept()
print("-"*25)
std2.display()
print("*"*25)


# ### Reverse String

# In[48]:


class Sentences:
    def __init__(self, sent=None):
        self.sent=sent
        self.vowelCount()
    def input(self):
        self.sent=input("Enter Sentance: ")
        self.vowelCount()
    def __reverse(self):
        words=self.sent.split()
        words.reverse()
        self.revSent=" ".join(words)
    def display(self):
        self.__reverse()
        print("Original String:", self.sent)
        print("Reversed String:", self.revSent)
    def vowelCount(self):
        self.count=0
        for i in self.sent:
            if i.lower() in 'aeiou':
                self.count+=1
    def __repr__(self):
        self.__reverse()
        return(self.sent+" --> "+self.revSent)



SentenceList = [Sentences(input(f"Enter Sentence#{i} : ")) for i in range(3)]
ReversedList = sorted(SentenceList , key = lambda x : x.count, reverse=True)
for sentence in ReversedList:
    print(sentence.count,"Vowels :",sentence)


# ### Reduce and lambda

# In[49]:


from functools import reduce
l = [int(input("Enter Numbers: ")) for i in range(6)]
print("Original List:",l)
ln = list(map(lambda X: X*3, l))
print("Multiplied List:", ln)

print("Sum of Original List Elements:", reduce(lambda x,y: x+y, l))
print("Sum of Multiplied List Elements:", reduce(lambda x,y: x+y, ln))


# ### List 1a

# In[50]:


list = input("Enter list elements  ")
list = list.split(" ")
list


# In[53]:


list = [int(i) for i in list]
list


# In[54]:


min(list)


# In[55]:


max(list)


# In[56]:


list.insert(3,7)


# In[57]:


list


# In[58]:


list.pop(3)
list


# In[60]:


ele = 32
if ele in list:
    print("present")
else:
    print("not present")


# ### Rectangle Class

# In[61]:


class Rectangle:
    def __init__(self, l, h):
        self.length = l
        self.height = h
        self.area = 0
    def __Area(self):
        self.area = self.length*self.height
    def printArea(self):
        self.__Area()
        print(self.area)

a=Rectangle(float(input("Enter Length: ")),float(input("Enter Width: ")))
a.printArea()


# 

# In[ ]:





# In[ ]:




