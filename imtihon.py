## 3- misol

# import datetime
# from datetime import date
# def kunlar_soni(sana1, sana2):
#     sana1 = date(*sana1)
#     sana2 = date(*sana2)
#     farq = sana2 - sana1
#     return farq.days
#
# sana1 = (2014, 7, 2)
# sana2 = (2014, 7, 11)
# print(kunlar_soni(sana1, sana2))


## 5-misol
# import datetime
# from datetime import datetime, timedelta
# bugun = datetime.now()
# kecha = bugun - timedelta(days=1)
# ertaga = bugun + timedelta(days=1)
# print("Kechagi sana:", kecha)
# print("Bugungi sana:", bugun)
# print("Ertangi sana:", ertaga)

## 6-misol
# L = [2, 2, 3, 4, 5]
# yangi_list = list(map(lambda x: x**3, L))
# print(yangi_list)


##1-misol

# class Student:
#     def __init__(self, student_id, student_name, class_name):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.class_name = class_name
#
#     def __str__(self):
#         return f"Raqami: {self.student_id}, Ismi: {self.student_name}, Fani: {self.class_name}"
# student1 = Student(1, "Javohir", "Matematika")
# student2 = Student(2, "Shunqor", "Fizika")
#
# print(student1)
# print(student2)

## 2-misol

# import json
# python_obj = {
#     "name": "David",
#     "class": "I",
#     "age": 6
# }
# json_obj = json.dumps(python_obj)
# print(json_obj)






















