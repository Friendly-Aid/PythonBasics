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

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


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

else:
    print("Invalid input")


