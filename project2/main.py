user_number = int(input("Enter a number: "))
if user_number % 4 == 0:
    print(f"{user_number} is a multiple of 4.")
elif user_number % 2 == 0:
    print(f"{user_number} is even.")
else:
    print(f"{user_number} is odd.")

num = int(input("Enter a number to check: "))   
check_num = int(input("Enter a number to divide by: "))
if num % check_num == 0:
    print(f"{num} is a multiple of {check_num}.")
else:
    print(f"{num} is not a multiple of {check_num}.")
