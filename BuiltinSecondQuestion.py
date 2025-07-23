
dict = {'name': "Atharva",
        'age': 10,
        'scores':[96,92,78,85]}

print(dict)

print("Keys of the dictionary dict is:",dict.keys())
print("values of the dictionary dict is:",dict.values())
print("Result by using items method:",dict.items())
print("The length of dictionary is:",len(dict))
print("Type of dictionary is:",type(dict))
print("Accessing dictionary by using get method:",dict.get('name'))

copy_dict = dict.copy()
print("Copied the dictionary dict by using copy method:",copy_dict)

x = ("Cricket","Volleyball")
y = (1,2)
print("Used the fromkeys method in dict:",dict.fromkeys(x,y))
print("Used pop method into copied dict:",copy_dict.pop("age"))
print("Used pop method into copied dict:",copy_dict.popitem())

print("Updated the age in dictionary:",dict.update({'age':10}))
dict['age'] = 7
print(dict)

result_string = eval(input("Enter the mathematical expression as string:"))
print(result_string)

print(f"The float value of above mathematical expression is:",float(result_string))
print(f"The float value of above mathematical expression is:",int(result_string))

print(type(dict['scores']))


list_to_str_join = ' '.join(str(item) for item in dict['scores'])
print(list_to_str_join)

reconverted_list = list(map(int, list_to_str_join.split()))

dict['scores'] = reconverted_list
print(dict)

scores = dict['scores']
subset_scores = scores[1:3]
print(f"Subset of scores (index 1 to 2): {subset_scores}")

number_range = [3.14, 5.8, 10.5, 7.2]
rounded_strings = []
for num in number_range:
    rounded_num = round(num)
    rounded_strings.append(str(rounded_num))
print(f"Rounded numbers converted to strings: {rounded_strings}")

scores = dict['scores']
print("First three scores (manual iteration):")
for i in range(3):
    print(scores[i])

empty_list = []
non_zero_number = 42
empty_string = ""

print(f"Truthiness of empty list: {bool(empty_list)}")
print(f"Truthiness of non-zero number: {bool(non_zero_number)}")
print(f"Truthiness of empty string: {bool(empty_string)}")
