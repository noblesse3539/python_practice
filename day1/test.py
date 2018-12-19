print("hello world")

lst = range(1,101)

even = []
odd = []

for i in lst:
    if i %2 == 0:
        even.append(i)
    else :
        odd.append(i)

print("list: ", lst)
print("even: ", even)
print("odd: ", odd)
