def check_6174(number):
    
    count=0
    while number != 6174:
        desc=int(''.join(sorted(str(number),reverse=True)))
        asc=int(''.join(sorted(str(number))))
       

        diff=desc - asc
        number=diff
        count+=1

    return "Constant 6174 found in",count,"iteratons"

print("Keep in mind that the number is inputted in 4 digits with at least any 2 different digits.")
num=int(input("Enter a 4-digit number: "))

if len(str(num)) != 4 or len(set(str(num))) < 2:
    print("Number should be of 4 digit")
else:
    print(check_6174(num))