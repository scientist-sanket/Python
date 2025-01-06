r a character: ")
vowels='aeiouAEIOU'
list=list(ch)
idx=0
for val in ch:
    if val in vowels:
        list.pop(idx)
        list.insert(idx,"@")
    idx+=1

result = "".join(list)
print(result)