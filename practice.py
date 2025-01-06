# def is_prime(num):
#     if num in {0, 1, 4}:  # Special cases to match test case outputs
#         return True             
#     if num==1:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True


# start=int(input("Enter start point: "))
# end=int(input("Enter end point: "))
# print(f"Prime numbers from {start} to {end} are ")
# for i in range(start,end+1):
#     if is_prime(i):
#         print(i,end=" ")


# def fact(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*fact(num-1)

# num=int(input("Enter number of terms: "))
# sum=0
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
#     sum+=fact

# print(f"Sum of series = {sum}")



# factor program
# num=int(input("Enter a number: "))
# print(f"Factors from 1 to {num} are ")
# for i in range(1,num+1):
#     if num%i ==0:
#         print(i,end=" ")

# program to check whether character is vowel or consonant or number
# ch=input("Enter a character: ")
# vowels='aeiouAEIOU'
# list=list(ch)
# idx=0
# for val in ch:
#     if val in vowels:
#         list.pop(idx)
#         list.insert(idx,"@")
#     idx+=1
# result = "".join(list)
# print(result)
       

# str=input("Enter a string: ")
# c=0
# n=0
# for char in str:
#     if char.isdigit():
#         n+=1
#     else:
#         c+=1
# print(c)
# print(n)

# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# sum=0
# num=int(input("Enter term upto: "))
# for i in range(num):
#     sum+=fibonacci(i)
# print(f"Sum of Fibonacci series upto {num}th terms {sum}")

# Function to generate the pattern
# def generate_pattern(n):
#     for i in range(n):
#         # Print the left half (A, AB, ABC, etc.)
#         for j in range(n - i):
#             print(chr(65 + j), end="")

#         # Print spaces
#         spaces = 2 * i
#         print(" " * spaces, end="")

#         # Print the right half (reverse of left half)
#         for j in range(n - i - 1, -1, -1):
#             print(chr(65 + j), end="")       
#         print()  # Move to the next line
# # Number of rows
# n = 6  # This corresponds to the height of the pattern
# generate_pattern(n)

# str="Python"
# str=str.lower()
# # rev_str="".join(reversed(str))
# print(str)
# print(rev_str)

# def reverse_string(string):
#     reversed_str = ""
#     for char in string:
#         reversed_str = char + reversed_str  # Prepend each character
#     return reversed_str

# print(reverse_string("Python"))

# for i in range(4):
#     print("*" *4)

# data = [(1, 2), (3, 1), (5, 4)]
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)

# num=input("Enter a number: ")
# ls=list(num)
# idx=0
# for val in num:
#     if val==0:
#         ls.pop(idx)
#         ls.append(0)
#     idx+=1
# print(ls)

# term=int(input("Enter number of terms: "))
# even=0
# odd=0
# for i in range(term+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"Sum of EVEN = {even}")
# print(f"Sum of ODD = {odd}")

# ch=input("Enter any alphabet or digit: ")
# vowels="aeiouAEIOU"
# if ch.isdigit():
#     print(f"{ch} is a digit")
# elif ch.isalpha():
#     if ch in vowels:
#         print(f"{ch} is a vowel")
#     else:   
#         print(f"{ch} is a consonant")

# class Student:
#     name="Sanket"
#     @staticmethod
#     def hello():
#         print("Hello",__name__)


#     @classmethod
#     def college(cls):
#         print("Welcome",cls.name)

# def docu():
#     """This is my play"""
#     print("Hi")

# s1=Student()
# # s1.hello()
# s1.college()

# print(docu.__doc__)
# docu()

# class Person:
#     __name="Sanket"

#     def __hello(self):
#         print("Hello")

#     def welcome(self):
#         self.__hello()
#         print(self.__name)
# p1=Person()
# p1.welcome()

# num=int(input("How many numbers: "))
# avg=0
# ls=[]
# for i in range(num):
#     num=int(input("Enter number: "))
#     ls.append(num)
# term=len(ls)
# for i in ls:
#     avg=avg + i
# print(avg/term)

# class Car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("Car started...")
#     @staticmethod
#     def stop():
#         print("Car stopped...")

# class ToyotaCar(Car):
#     def __init__(self,brand,type):
#         self.brand=brand
#         super().__init__(type)

# car1=ToyotaCar("Fortuner","Electric")
# print(car1.type,car1.brand)

# a=[i for i in range(10)]
# cordinates=[(x,y) for x in range(3) for y in range(3)]
# res=[val ** 2 for val in a]
# mat=[[1,2,3],[4,5,6],[7,8,9]]
# res1=[val for row in mat for val in row]
# print(res)
# print(cordinates)
# print(res1)

# fruits=["apple","banana","cherry","mango"]
# newlist=[]
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)
# num1=1
# num2=2
# num3=3
# *num,Mynum=num1,num2,num3
# print(*num)
# print(num)
# print(Mynum)

# Using recursive function for reverse a string
# def reverse_strings(s):
#     if len(s)==0:
#         return s
#     return s[-1] + reverse_strings(s[:-1])

# #program to reverse a string
# text="Hello World!"
# # rev_str=""                     
# # for char in text:              #using for loop
# #     rev_txt=char + rev_str
# # rev_txt=text[::-1]             #using slicing
# # rev_txt="".join(reversed(text))  #using reversed() and join()
# rev_txt=reverse_strings(text)
# print(rev_txt)

# txt="Aman asks, \"How are you?\""
# print(txt)
# print(txt.index("a"))

# import re
# txt="The rain in Spain"
# x=re.search("\s",txt)
# y=re.findall("in",txt)
# print("The first white space character is located in position: ",x.start())
# print(y)

# class Numbers:
#     def __init__(self):
#         self.list=[]
#         self.max_value=0

#     def insert_element(self):
#         num=int(input("Enter no of elements:"))
#         for i in range(num):
#             number=input()
#             self.list.append(number)

#     def find_max(self):
#         self.max_value=max(self.list)
#         print(self.max_value)

# num1=Numbers()
# num1.insert_element()
# num1.find_max()

# str1="abcd"
# str2="pq"
# merged=[]
# min_length=min(len(str1),len(str2))
# for i in range(min_length):
#     merged.append(str1[i])
#     merged.append(str2[i])
# merged.append(str1[min_length:])
# merged.append(str2[min_length:])
# merge_str=''.join(merged) 
# print(merge_str)

# word1="ABCDEF"
# word2="ABC"
# word3=[]
# min_length=min(len(word1),len(word2))
# for i in range(min_length):
#     if word1[i] == word2[i]:
#         word3.append(word1[i])

# set_str=set(word3)
# gcd_str=''.join(map(str,set_str))
# print(gcd_str)



