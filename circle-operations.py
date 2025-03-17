import math

def calculate_circle_area(r):
    return math.pi*r**2

def calculate_circle_circumference(r):
    return 2*math.pi*r

def try_again(accept,prompt):
    while True:
        t=input(prompt).lower()
        if t in list(accept):
            return t
        else:
            print("Invalid choice.\n")

go="y"

save_info=[]

while go=="y":
    val=try_again("12","options:\n1: calculate circle area\n2: calculate circle circumference\n\nplease enter your choice: ")
    r=None
    while not r:
        try:
            r=float(input("enter radius: "))
        except Exception as exception:
            print("please enter a valid number.\n")
    print()

    if val=="1":
        result=f"the area of a circle with radius {r:.2f} is {calculate_circle_area(r):.2f}"
        print(result)
        print()
        if result not in save_info:
            save_info.append(result)

    elif val=="2":
        result = f"the circumference of a circle with radius {r:.2f} is {calculate_circle_circumference(r):.2f}"
        print(result)
        print()
        if result not in save_info:
            save_info.append(result)

    go=try_again("yn","Do you want to go again? y/n: ")
    print()

import os

save_file=os.path.join(os.getcwd(),"circle_results.txt")
with open(save_file,"w") as f:
    for info in save_info:
        f.write(info+"\n")