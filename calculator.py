
#declaring a function for the addition operation
def addtion(numbers):
    answer = sum(numbers)
    print(f"The addition of the numbers is---> {answer}")

#declaring a function for the subtraction operation
def subtraction(numbers):
    answer = numbers[0]
    for num in numbers[1:]:
        answer -= num
    print(f"The addition of the numbers is---> {answer}")

#declaring a function for the multiplication operation
def multiplication(numbers):
    answer = numbers[0]
    for num in numbers[1:]:
        answer *= num
    print(f"The multiplication of the numbers is---> {answer}")

#declaring a function for the division operation
def division(numbers):
    if 0 in numbers[1:]:
        print("Math Error, Division by zero is not allowed")
    else:
        answer = numbers[0]
        for num in numbers[1:]:
            answer /= num
        print(f"The division of the numbers is---> {answer}")

#declaring a function for the welcome message
def welcome_message():
 while True:
    print("---------------------------------")
    print("Welcome to the calculator program")
    print("---------------------------------")
    print("Please select the operation you want to perform")
    print(" ")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    print(" ")

   
    option = input("Please enter aany option to perform calculation on---> ").lower()

    if option in "a":
            print("-----------------------------------------")
            print("You are welcome to the addition operation")
            print("-----------------------------------------")
            count = int(input("How many numbers do you want to add---> "))
            numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
            #function call
            addtion(numbers)

    elif option in "b":
            print("-----------------------------------------")
            print("You are welcome to the subtraction operation")
            print("-----------------------------------------")
            count = int(input("How many numbers do you want to subtract---> "))
            numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
            #function call
            subtraction(numbers)

    elif option in "c":
            print("-----------------------------------------")
            print("You are welcome to the multiplication operation")
            print("-----------------------------------------")
            count = int(input("How many numbers do you want to multiply---> "))
            numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
            #function call
            multiplication(numbers)
        
    elif option in "d":
            print("-----------------------------------------")
            print("You are welcome to the division operation")
            print("-----------------------------------------")
            count = int(input("How many numbers do you want to divide---> "))
            numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
            #function call
            division(numbers)

    elif option in "e":
            print("Thank you for using the calculator program \nExisting the Calculator, Goodbye!!! :)")
            break

    else:
            print("Invalid option, please select a valid option")

    cont = input("Do you want to continue (yes/no)---> ").lower()
    if cont not in "yes":
            print("Thank you for using the calculator program \nExisting the Calculator, Goodbye!!! :)")
            break

        

#function call for main message
welcome_message()



