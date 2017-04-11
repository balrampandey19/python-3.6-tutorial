my_var = "hello"

print(my_var[0])
for cc in my_var:
    print(cc)


my_list = [10,20,30,40,50]

for num in my_list:
    print(num)


user_want_number = True

while user_want_number == True:
    print(10)
    user_input= input("Do you want to print again (y/n)")

    if(user_input == 'n'):
     user_want_number = False
