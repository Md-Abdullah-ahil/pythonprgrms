li=[2,3,4,55,56,78,75,69,66,101,100]
odd=0
even=0
for x in li:
    if x%2 == 0:
        even +=1
    else:
        odd += 1

print(li)
print("total even numbers in the list:",even)
print("total odd numbers in the list :",odd)
