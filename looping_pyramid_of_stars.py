user_input = int(input("How many layers do you want in your pyramid of stars? "))

times = 1

while times <= user_input:
    print("*" * times)
    times += 1