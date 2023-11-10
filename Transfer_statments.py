#break
#continue
#pass

#>break statement
#based on some condition if we want to break loop excecution

# for i in range (10):
#     if i==8:
#         print("hii")
#         print("hello")
#         break
#     print(i)
#     print("bottle")

# print("bagunava")



# cart=[10,30,400,800,70,90]
# for item in cart:
#     if item>500:
#         print("product price excced the limit",item)
#         continue
#     print("processing items susscefully ",item)


# for i in range(20):
#     if i%2!=0:
#         continue
#     print(i)


#pass statement

# for i in range(100):
#     if i%10==0:
#         print(i)
#     else:
#         pass
# print("hi aman")



#various places to declare static var
# 1. inside a class directly 
# class Student:
#     a=900
# t=Student()
# print(t.a)

#2. inside the constructor by using classname
# class Student:
#     def __init__(self):
#         Student.a=800    
# t=Student()
# print(t.a)

#3.inside method by using class name 
# class Student:
#     def __init__(self):
#         pass
#     def m1(self):
#         Student.a=700
            
# t=Student()
# print(t.a)

#4. inside class method by using cls var or class name 
# class Student:
#     def __init__(self):
#         pass
#     def m1(self):
#         pass
#     @classmethod
#     def m2(cls):
#         Student.a=600
#         cls.e=1000

            
# t=Student()
# print(t.a)


#5.inside static method by using classname 
# class Student:
#     def __init__(self):
#         pass
#     def m1(self):
#         pass
#     @classmethod
#     def m2(cls):
#         Student.a=600
#         cls.e=1000

#     @staticmethod 
#     def m3(self):
#         self.a=900
#         Student.y=2000
            
# t=Student()
# print(t.a)

#6. from outside of the class also by using classname
# class Student:
    
#     def __init__(self):
#         pass
#     def m1(self):
#         pass
#     @classmethod
#     def m2(cls):
#         Student.a=600
#         cls.e=1000

#     @staticmethod 
#     def m3(self):
#         self.a=900
#         Student.y=2000
            
# t=Student()
# print(t.a)
# Student.r=7000


# class Student:
#     a=800
#     def __init__(self):
#         Student.b=400
#     def m1(self):
#         Student.c=500
#     @classmethod
#     def m2(cls):
#         Student.d=600
#         cls.e=1000

#     @staticmethod 
#     def m3():
#         Student.f=2000

# t=Student()
# Student.m1()
# print(Student.__dict__)


class emp:
    def __int__(self):
        pass
    def m1():
        print("hello")