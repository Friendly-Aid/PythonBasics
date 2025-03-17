x = 10
y = 20.5
name = "Alice"
my_list = [1, 2, 3, 4]
is_valid = True

print(type(x))
print(type(y))
print(type(name))
print(type(my_list))
print(type(is_valid))
print()

a=5
b=10

print(f"a is {a} b is {b}")
a,b=b,a
print(f"a is {a} b is {b}")
print()

numbers = [5, 10, 15, 20, 25]
numbers.append(30)
numbers.remove(15)
numbers.sort(reverse=True)
print(numbers)
print()

student = {"name": "John", "age": 20, "grade": "A"}

student["age"]=21
student["major"]="Computer Science"
del student["grade"]
print(student)
print()

num1 = float(input("enter num1: "))
num2 = float(input("enter num2: "))
print(num1+num2)
print(abs(num1-num2))
print(num1*num2)
print(num1/num2)
print("num1 is greater than num2" if num1>num2 else "num1 is less than num2")
print()

person = ("Alice", 30, "Engineer")
name,age,profession = person
print(name)
print(age)
print(profession)