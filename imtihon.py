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


# import datetime
#
# def yakshanba(year):
#     yakshanba1 = datetime.date(2025, 1, 5)
#     date = yakshanba1
#     while date.year == year:
#         print(date)
#         date += datetime.timedelta(days=7)
#
# yakshanba(2025)

# from collections import Counter
#
# def sozlar(filename):
#     with open(filename, 'r') as file:
#         text = file.read()
#     words = text.split()
#     word_count = Counter(words)
#     return dict(word_count)
#
# filename = 'context.txt'
# word_counts = sozlar(filename)
# print(word_counts)

#
# def tub_sonlar(n):
#     tub_sonlar = []
#     for son in range(2, n + 1):
#         tub = True
#         for i in range(2, int(son ** 0.5) + 1):
#             if son % i == 0:
#                 tub = False
#                 break
#         if tub:
#             tub_sonlar.append(son)
#     return tub_sonlar
#
# n = 20
# print(tub_sonlar(n))




# class Solution:
#     def twoSum(self, nums, target):
#         for a in range(len(nums)):
#             for b in range(a + 1, len(nums)):
#                 if nums[a] + nums[b] == target:
#                     return [a, b]
#         return []
#
# nums = [3, 2, 4]
# target = 6
# solution = Solution()
# print(solution.twoSum(nums, target))
#
# class Solution:
#     def twoSum(self, nums, target):
#         for a in range(len(nums)):
#             for b in range(a + 1, len(nums)):
#                 if nums[a] + nums[b] == target:
#                     return [a, b]
#         return []
#
# nums = [3,3]
# target = 6
# solution = Solution()
# print(solution.twoSum(nums, target))

# class Solution:
#     def twoSum(self, nums, target):
#         for a in range(len(nums)):
#             for b in range(a + 1, len(nums)):
#                 if nums[a] + nums[b] == target:
#                     return [a, b]
#         return []
# nums = [2,7,11,15]
# target = 9
# solution = Solution()
# print(solution.twoSum(nums, target))


# class Solution:
#     def isAnagram(self, s: str, t: str):
#         return sorted(s) == sorted(t)
# s = "anagram"
# t = "nagaram"
# print(Solution.isAnagram())

# def is_anagram(s,t):
#     return sorted(s) == sorted(t)
# print(is_anagram("anagram", "nagaram"))

# def is_anagram(s:str,t:str):
#     if len(s) !=len(t):
#         return False
#     s_data = {}
#     t_data = {}
#     for i in range(0,len(s)):
#         s_data[s[i]] = 1 + s_data.get(s[i], 0)
#         t_data[t[i]] = 1 + t_data.get(t[i], 0)
#
#     return s_data == t_data
#
# print(is_anagram("anagram","nagaram"))

### 202 misol Letcode


# def isHappy( n: int) -> bool:
#     seen = set()
#     cuur = str(n)
#     while cuur not in seen:
#         seen.add(cuur)
#         summ = 0
#         for digit in cuur:
#             summ+=int(digit)**2
#
#         if summ==1:
#             return True
#         cuur=str(summ)
#     return False
#
# print(isHappy(19))

#
# class Solution:
#     def searchInsert(self, nums: int, target: int) -> int:
#
#         for i in range(len(nums)):
#             if nums[i] >= target:
#                 return i
#         return len(nums)
# nums = [1, 3, 5, 6]
# target = 5
# print(Solution.searchInsert(nums, target))

#
# def nima_gap(nums):
#     return len(nums) != len(set(nums))
#
# nums = [1, 2, 3, 1]
# print(nima_gap(nums))
#
# def qondaye(nums):
#     son = set()
#     for num in nums:
#         if num in son:
#             return True
#         son.add(num)
#     return False
# nums = [1, 2, 3, 1]
# print(qondaye(nums))

# def sonlar(nums, target):
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return left
#
# nums = [1, 3, 5, 6]
# target = 5
# print(sonlar(nums, target))

#
# def my_sqrt(x):
#     yangi = x
#     i = 0
#     result = 0
#     while i <= yangi:
#         a = i*i
#         if a <= x:
#             result = i
#         else:
#             break
#         i += 1
#
#     return result
# print(my_sqrt(8))

# def qondaye(nums):
#     son = set()
#     for num in nums:
#         if num in son:
#             return True
#         son.add(num)
#     return False
# nums = [1, 2, 3, 1]
# print(qondaye(nums))


# import math
#
#
# def mySqrt(x):
#
#     if x == 0:
#         return 0
#     else:
#         b = x**0.5
#         return   int(math.floor(b))
#
# natija = mySqrt(x=10)
# print(natija)
#
# def climb_stairs(n):
#     if n <= 2:
#         return n
#     a, b = 1, 2
#     for _ in range(3, n + 1):
#         a, b = b, a + b
#     return b
#
# n = 2
# print(climb_stairs(n))
#
#
# def computer_guesses():
#     low = 1
#     high = 10
#     attempts = 0
#     while True:
#         guess = (low + high) // 2
#         attempts += 1
#         print(f"Kompyuter {guess} sonini o'yladi.")
#         feedback = input("Bu son to'g'rimi (t), kichikroq (k), yoki kattaroq (K)? ")
#         if feedback == 't':
#             print(f"Kompyuter {attempts} urinishda sonni topdi.")
#             break
#         elif feedback == 'k':
#             high = guess - 1
#         elif feedback == 'K':
#             low = guess + 1
#
# computer_guesses()
#
# def remove_spaces_and_punctuation(input_string):
#     # Belgilarni va bo'sh joylarni o'chirish
#     cleaned_string = ''.join(char for char in input_string if char.isalnum())
#     return cleaned_string
#
# # Misol
# input_string = "AI-powered spreadsheets help you and your team manage, visualize and analyze data."
# output_string = remove_spaces_and_punctuation(input_string)
# print(output_string)
#
#
# class User:
#     def __init__(self, name, status):
#         self.name = name
#         self.status = status
#
# class Exam:
#     def __init__(self, student, teacher, score):
#         self.student = student
#         self.teacher = teacher
#         self.__score = score
#
#     def get_score(self, user):
#         if user.status == 'teacher' or user == self.student:
#             return self.__score
#         else:
#             return "Sizda bahoni ko'rish huquqi yo'q"
#
#     def set_score(self, user, new_score):
#         if user.status == 'teacher':
#             self.__score = new_score
#         else:
#             return "Sizda bahoni tahrirlash huquqi yo'q"
#
# # Misol uchun
# student = User("Ali", "student")
# teacher = User("Vali", "teacher")
# exam = Exam(student, teacher, 85)
#
# print(exam.get_score(student))  # 85
# print(exam.get_score(teacher))  # 85
# print(exam.set_score(student, 90))  # Sizda bahoni tahrirlash huquqi yo'q
# print(exam.set_score(teacher, 90))  # None (bahoni tahrirlaydi)
# print(exam.get_score(student))  # 90
#
#
#
#
# import random
#
# def tanlangan():
#     number = random.randint(1, 10)
#     attempts = 0
#     while True:
#         son = int(input("1 dan 10 gacha bo'lgan sonni kiriting: "))
#         attempts += 1
#         if son < number:
#             print("Kiritilgan son kichikroq.")
#         elif son > number:
#             print



def recursive_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))




























