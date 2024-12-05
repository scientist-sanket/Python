#default constructor
# def __init__(self):
#     pass

# wap to take name and marks of 3 subjects as parameter in constructor name print the average in method
# class Student:
#     def __init__(self,name,marks):  #parametrized constructor
#         self.name=name
#         self.marks=marks
    
#     def avg(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         average=sum/3
#         print(f"Average of marks : {average}")

# s1=Student("Sanket",[40,88,76])
# s1.avg()

#STatic method example
# class s_method:
#     @staticmethod
#     def hello():
#         print("Hello World")

#     def welcome():
#         print("Welcome sir")

# s=s_method()
# s.hello()
# s.welcome()

#Bank operation through OOPS concept
# class Account:
#     def __init__(self,name,acc,bal):
#         self.name=name
#         self.acc_no=acc
#         self.balance=bal

#     #credit method
#     def credit(self,amount):
#         self.balance += amount
#         print(f"Account {self.acc_no} is credit with amount Rs. {amount}")
#         print(f"Total Balance = {self.get_balance()}")

#     #debit method
#     def debit(self,amount):
#         self.balance -= amount
#         print(f"Account {self.acc_no} is debited with amount Rs. {amount}")
#         print(f"Total Balance = {self.get_balance()}")

#     def get_balance(self):
#         return self.balance

# cust1=Account("Akash",87690,2000)
# cust1.debit(600)
# cust1.credit(4000)
# cust1.debit(2000)
# cust1.credit(299)

# cust2=Account("Motu",65473,500)
# cust2.debit(100)
# cust2.credit(50)
# cust2.credit(20)
# cust2.debit(49)
