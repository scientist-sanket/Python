# with open("practice.txt","w") as f:
#     f.write("Hi Everyone\n")
#     f.write("we are learning File I/O \nusing Java.")
#     f.write("\nI like programming in Java.")


# Function to replace occurrence of "Java" with "Python"
# def replace_word():
#     with open("practice.txt","r") as f:
#         data=f.read()

#         new_data=data.replace("Java","Python")
#         print(new_data)

#     with open("practice.txt","w") as s:
#         s.write(new_data)


# Search if the word "learning" exists in the file or not
# word="learning"

# with open("practice.txt","r") as f:
#     data=f.read()
#     if(word in data):
#         print("Found")
#     else:
#         print("Not Found")

# Function to find in which line of the file does the word "learning" occur first. Print -1 if word not found
# def search_on_line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data =f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1

#         print(-1)

# From a file containing numbers separated by comma, print the count of even numbers
# with open("number.txt","w") as f:
#     f.write("1,4,8,69,50,101")
#     f.close()
# count=1
# with open("number.txt","r") as f:
#     data=f.read()
#     list=data.split(",")

#     print(list)

#     for el in list:
#         if(int(el) % 2 == 0):
#             count+=1

# print(count)

        