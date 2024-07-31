#problem 1
numbers = [10, 20, 30, 40, 50]
total_sum = sum(numbers)
print(f"The sum of all items in the list is: {total_sum}")


#problem 2
numbers = [10, 20, 4, 45, 99, 67]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print(f"The largest number in the list is: {largest}")
print(f"The smallest number in the list is: {smallest}")


#problem 3
numbers = [10, 20, 30, 10, 20, 40, 50, 30, 60]
seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print("Duplicate values in the list are:")
print(duplicates)


#problem 4
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3
first_part = original_list[:length_of_first_part]
second_part = original_list[length_of_first_part:]
print("Original list:")
print(original_list)
print(f"Length of the first part of the list: {length_of_first_part}")
print("Splitted the said list into two parts:")
print(f"First part: {first_part}")
print(f"Second part: {second_part}")


#problem 5
original_list = ['red', 'green', 'white', 'black']
print("Traverse the list in reverse order:")
for index in range(len(original_list) - 1, -1, -1):
    print(original_list[index])


#problem 6
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
values = test_dict.values()
mean = sum(values) / len(values)
print(f"The mean of the values in the dictionary is: {mean}")


#problem 7
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
combined_dic = {**dic1, **dic2, **dic3}
print("Concatenated dictionary:")
print(combined_dic)


#problem 8
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Keys in the dictionary:")
for key in dict_num.keys():
    print(key)
print("\nValues in the dictionary:")
for value in dict_num.values():
    print(value)
print("\nKey-Value pairs in the dictionary:")
for key, value in dict_num.items():
    print(f"Key: {key}, Value: {value}")


#problem 9
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
print("Keys in the dictionary:")
for key in input_dict.keys():
    print(key)
print("\nValues in the dictionary:")
for value in input_dict.values():
    print(value)
print("\nKey-Value pairs in the dictionary:")
for key, value in input_dict.items():
    print(f"Key: {key}, Value: {value}")


#problem 10
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
count_4 = tuplex.count(4)
print(f"The number 4 appears {count_4} times in the tuple.")


#problem 11
listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)
print("Original list:")
print(listx)
print("Converted tuple:")
print(tuplex)


#problem 12
tuples_list = [(1, 2), (3, 4), (5, 6)]
total_sum = 0

for tup in tuples_list:
    for num in tup:
        total_sum += num
print(f"The sum of the numbers in the given tuple is: {total_sum}")


#problem 13
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
employees = [employee1, employee2, employee3]
print("Employee Records:\n")
for emp in employees:
    name, emp_id, department, salary = emp
    print(f"Name : {name}")
    print(f"Employee ID : {emp_id}")
    print(f"Department : {department}")
    print(f"Salary : {salary}")
    print()  # Print a blank line between records


#problem 14
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_items = (set1 - set2) | (set2 - set1)
print("Unique items from both sets:")
print(unique_items)


#problem 15
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_elements = set1 ^ set2
print("Elements present in either set1 or set2, but not both:")
print(unique_elements)


#problem 16
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
common_elements = set1 & set2
if common_elements:
    print("Common elements in both sets:")
    print(common_elements)
else:
    print("No common elements in both sets.")


#problem 17
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
common_elements = set1 & set2
set1.intersection_update(set2)
print("Updated set1 with only common elements:")
print(set1)
