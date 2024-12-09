print("Before inputting the number, Please mind that the first digit should not be equal to third digit")
a=int(input("Enter a three-digit number: "))

if len(str(a)) == 3:
    a_num=str(a)
    first_digit=a_num[0]
    last_digit=a_num[2]
    
    if(first_digit==last_digit):
        print("Enter a valid 3-digit number")
    else:
        a_sorted_num =int(''.join(sorted(a_num)))
        d_sorted_num = int(''.join(sorted(a_num,reverse=True)))

        print(a_sorted_num)
        print(d_sorted_num)

        diff=(d_sorted_num) - (a_sorted_num)

        rev_diff=int(''.join(reversed(str(diff))))
        print(rev_diff)

        add=(diff) + (rev_diff)

        print(add)
else:
    print("Not a 3 digit number")




