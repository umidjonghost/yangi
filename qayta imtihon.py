### 6-misol
from dataclasses import replace


# def toq_son(n):
#     return n % 2 != 0
# print(toq_son(5))
# print(toq_son(4))


### 2-misol
#
# class User:
#     def __init__(self, name, status):
#         self.name = name
#         self.status = status
#
# class Exam:
#     def __init__(self, student , teacher , bal):
#         self.student = student
#         self.teacher = teacher
#         self.__bal = bal
#
#     def get_bal(self, user):
#         if user.status == "teacher" or user == self.student:
#             return self.__bal
#
#         else:
#             return "Siz balni kora olmaysiz"
#
#     def yangi_bal(self, user, yangibal):
#         if user.status == 'teacher':
#             self.__bal = yangibal
#
#         return "Siz balni ozgartira olmaysiz"
#
# student1 = User("Javohir", "student")
# teacher1 = User("Shohjahon", "teacher")
# exam = Exam(student1, teacher1, 85)
#
# print(exam.get_bal(student1))
# print(exam.yangi_bal(student1, 90))
#

## 8-misol
#
# import random
# def tanlangan_son():
#     son = random.randint(1,10)
#
#     while True:
#         son1 = int(input("1 dan 10 gacha raqam tanlang: "))
#
#         if son1 < son:
#             print("kattaroq son kiriting: ")
#         elif son1 > son:
#             print("kichikroq son kiriting: ")
#         else:
#             print("siz togri topdingiz!")
#
# tanlangan_son()

## 7-misol

# def list_yigindi(list):
#     if not list:
#         return 0
#     else:
#         return list[0] + list_yigindi(list[1:])
#
# son = [1,2,3,4,5]
# print(list_yigindi(son))

## 5-misol
# def setter(list):
#     replace('-','')
#     replace(' ','')
#     replace(',','')
#
# print(setter("AI-powered spreadsheets help you and your team manage, visualize and analyze data."))
#
# setter()














