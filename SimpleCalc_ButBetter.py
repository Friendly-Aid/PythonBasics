def Add(x,y):
    return x+y
def Subtract(x,y):
    return x-y
def Multiply(x,y):
    return x*y
def Divide(x,y):
    if y==0:
        return "Error: Division by zero!"
    return x/y


while True:
    choice=None
    while choice not in list("1234"):
        print("\nSelect operation:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide\n")
        choice = input("Enter choice (1/2/3/4): ")
        if choice not in list("1234"):
            choice=input(f"Sorry {choice} is not a valid operation. Try again? Y/n: ").lower()[0]
            if choice == "n":
                print("\nOK! Exiting program.")
                exit()
            elif choice != "y":
                while choice != "y":
                    choice=input("Y/n prompts only accept Y or N. Please enter Y or N: ").lower()[0]
                    if choice == "n":
                        print("\nOK! Exiting program.")
                        exit()


    num1=None
    while not isinstance(num1,float):
        try:
            num1 = float(input("\nPlease enter the first number: "))
        except:
            num1 = input(f"Sorry but {num1} is not a valid number. Try again? Y/n: ").lower()[0]
            if num1 == "n":
                print("\nOK! Exiting program.")
                exit()
            else:
                while num1 != "y":
                    num1 = input("Y/n prompts only accept Y or N. Please enter Y or N: ").lower()[0]
                    if num1 == "n":
                        print("\nOK! Exiting program.")
                        exit()

    num2 = None
    while not isinstance(num2, float):
        try:
            num2 = float(input("Please enter the second number: "))
            print()
        except:
            num2 = input(f"Sorry {num2} is not a valid number. Try again? Y/n: ").lower()[0]
            if num2 == "n":
                print("\nOK! Exiting program.")
                exit()
            elif num2 == "y":
                print()
            else:
                while num2 != "y":
                    num2 = input("Y/n prompts only accept Y or N. Please enter Y or N: ").lower()[0]
                    if num2 == "n":
                        print("\nOK! Exiting program.")
                        exit()
                    elif num2=="y":
                        print()

    if choice=='1':
        result=Add(num1,num2)
        print(f"{num1} + {num2} = {result}")

    elif choice=='2':
        result=Subtract(num1,num2)
        print(f"{num1} - {num2} = {result}")

    elif choice=='3':
        result=Multiply(num1,num2)
        print(f"{num1} * {num2} = {result}")

    elif choice=='4':
        result=Divide(num1,num2)
        if isinstance(result,str):
            print(result)
        else:
            print(f"{num1} / {num2} = {result}")

    go=input("\nWould you like to go again? Y/n: ").lower()[0]

    if go == "n":
        print("\nOK! Exiting program.")
        exit()
    else:
        while go != "y":
            go = input("Y/n prompts only accept Y or N. Please enter Y or N: ").lower()[0]
            if go == "n":
                print("\nOK! Exiting program.")
                exit()