user_list=input("Enter a list of numbers separated by spaces: ")
list_num = list(map(int, user_list.split())) 
sorted_list = sorted(list_num) 
check_num = int(input("Enter a number to check if it's in the list: "))
if check_num in sorted_list:
    print(f"{check_num} is in the list.")
else:
    print(f"{check_num} is not in the list.")
print(f"Sorted list: {sorted_list}")
