user_input = input("Enter numbers separated by spaces: ")  
list_num = user_input.split() 
new_list = [list_num[0], list_num[-1]]
print(new_list)
