# function to check number whether is even or odd
# def even_odd(n):
#     if(n%2==0):
#         print("EVEN")
#     else:
#         print("ODD")

# even_odd(4)

# function to convert usd to inr
# def usd_inr(usd_val):
#     inr_val=usd_val * 87
#     print(usd_val,"USD =",inr_val,"INR")

# usd_inr(85)

# function to fnd the factorial of n .
# def calc_fact(n):
#     fact=1
#     for el in range(1,n+1):
#         fact*=el
#     print("Factorial= ",fact)

# calc_fact(6)

# Function to print the elements of a list in a single line
# states=["Bihar","Assam","Himachal Pradesh"]

# def print_el(list):
#     for el in list:
#         print(el,end=" ")

# print_el(states)

# Function to print the length of a list.
# student=["Sanket",21,"MCA","Wipro"]

# def print_len(list):
#     print(len(list))

# print_len(student)

# Recursive function to print from n to 1
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# Recursive function to find the factorial of any number
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1) * n

# print(fact(6))

# Recursive function to calculate the sum of first n natural number
# def sum(n):
#     if(n==0):
#         return 0
#     return (sum(n-1) + n)

# print(sum(10))

# Recusive function to print the elements of a list
# def print_list(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)

# fruits=["apple","pomegrante","guava"]

# print_list(fruits)