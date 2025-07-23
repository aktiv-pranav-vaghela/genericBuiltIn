lst = []

try:
    numbers_str = input("Please enter a series of numbers, separated by commas (e.g., 10, 25, 5, 30, 15): ")
    lst = [int(num.strip()) for num in numbers_str.split(',')]
except ValueError:
    print("Invalid input. Please ensure you enter only numbers separated by commas.")
print(f"You entered: {lst}")

lst = list(filter(lambda x:x > 10,lst))
print("All numbers are greater than 10:",lst)

print("The numbers are greater than 10 and even:",list(filter(lambda x:x % 2 == 0,lst)))
print("The numbers are greater than 10,even and also divisible by 5:",list(filter(lambda x:(x / 5 == 0),lst)))

try:

    print("The maximum value of list is" ,max(lst))
except ValueError:
    print("Filtered List is empty,hence won't have any maximum value.")

try:
    print("The minimum value of list is" ,min(lst))
except ValueError:
    print("Filtered List is empty,hence won't have any maximum value.")

print("The sum value of list is" ,sum(lst))

print("List in Ascending order",sorted(lst,reverse=False))
print("List in descending order",sorted(lst,reverse=True))

print(f"The tuple of the above list is: {tuple(lst)}")
print(f"The tuple of the above list is: {set(lst)}")
print("Is List used is of type list?:",isinstance(lst,list))

print("Is List changed into tuple?:",isinstance(tuple(lst),tuple))

# print("The square of each element of the list is:",list(filter(lambda x:(x ** 2),lst)))
y = list(map(lambda x:(x ** 2),lst))
print("The square of each element of the list is:",y)

