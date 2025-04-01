output_file="user_info.txt"

def categorize_age(age):
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

while True:
    name=input("Enter your name: ")
    age=None

    while type(age)!=int:
        try:
            age=int(input("Enter your age: "))
            if age < 0:
                age=None
                raise "bad_age"
        except Exception as e:
            print("Please enter a valid age")

    age_type=categorize_age(age)

    print(f"{age_type}: {name} is {age} years old")

    with open(output_file,"a") as f:
        f.write(f"{age_type}: {name} is {age} years old\n")

    while True:
        rerun=input("Do you want to run the program again? (y/n): ").lower().strip()
        if rerun[0] == "y":
            break
        elif rerun[0] == "n":
            print("Exiting program.")
            exit()
        else:
            print("Please enter y or n")
