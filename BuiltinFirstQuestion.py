lst = []

for i in range(1,5):
    numbers = int(input("Enter the numbers: "))
    lst.append(numbers)
print(lst)

lst = list(filter(lambda x:x > 10,lst))
print("All numbers are greater than 10:",lst)

print("The numbers are greater than 10 and even:",list(filter(lambda x:x % 2 == 0,lst)))
print("The numbers are greater than 10,even and also divisible by 5:",list(filter(lambda x:(x / 5 == 0),lst)))
print("The max value of list is" ,max(lst))
print("The min value of list is" ,min(lst))
print("The sum value of list is" ,sum(lst))

print("List in Ascending order",sorted(lst,reverse=False))
print("List in descending order",sorted(lst,reverse=True))

print(tuple(lst))
print(set(lst))
print("Is List used is of type list?:",isinstance(lst,list))
print("Is List changed into tuple?:",isinstance(tuple(lst),tuple))

print("The square of each element of the list is:",list(filter(lambda x:(x ** 2),lst)))
y = list(map(lambda x:(x ** 2),lst))
print(y)

