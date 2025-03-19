import sqlite3
import os

def yes_no(prompt) -> str:
    yn = input(prompt).lower()
    while yn not in 'yn':
        yn = input("Invalid Input. Please enter y or n.").lower()[0]
    return yn

remake=False
if not os.path.exists('contacts.db'):
    with open('../PyCharmMiscProject/contacts.db', 'wb') as f:
        pass
    remake=True

contacts=sqlite3.connect('contacts.db')
contacts_exec=contacts.cursor()

if remake:
    contacts_exec.execute('''
        CREATE TABLE contacts(number INTEGER, name TEXT, email TEXT)
    ''')
    contacts.commit()

while True:
    if yes_no("Do you want to enter the Contact Management System? y/n ") == "n":
        break
    print("\nContact Management System")
    print("\n1 - Add Contact")
    print("\n2 - Edit Contact")
    print("\n3 - Delete Contact")
    print("\n4 - Find Contact")
    choice=input("\nEnter any key to continue: ")
    print()
    while choice not in "1234":
        print("Invalid Input. please enter a number from 1-4: ")
        continue
    if choice=="1":
        name = input("Enter Contact Name: ").lower()
        contacts_exec.execute("SELECT name FROM contacts WHERE name=?", (name,))
        valid_name = contacts_exec.fetchone()
        if valid_name:
            print(f"\nContact with name '{name}' already exists.\n")
            continue
        number=None
        while number is None:
            try:
                number=int(input("\nEnter Contact Number: ").replace(" ",""))
            except Exception as e:
                print("Invalid Input. Please enter a valid number.")
        email=input("\nEnter Contact Email: ").lower()
        contacts_exec.execute("INSERT INTO contacts VALUES (?,?,?)",(number,name,email,))
        contacts.commit()
        print(f"\nContact {name} has been added")

    elif choice=="2":
        name=input("Enter Current Contact Name: ").lower()
        contacts_exec.execute("SELECT name FROM contacts WHERE name=?",(name,))
        valid_name=contacts_exec.fetchone()
        while valid_name == None:
            retry=yes_no("The name you gave is not in the database. DO you want to try again? ")
            if retry == "y":
                name=input("Enter Current Contact Name: ").lower()
            elif retry == "n":
                continue
            else:
                contacts_exec.execute("SELECT name FROM contacts WHERE name=?", (name,))
                valid_name = contacts_exec.fetchone()

        change=yes_no("\nDo you want to change their number? (y/n) ")
        if change=="y":
            number = None
            while number is None:
                try:
                    number = int(input("\nEnter New Number: ").replace(" ", ""))
                except Exception as e:
                    print("Invalid Input. Please enter a valid number.")
            contacts_exec.execute("UPDATE contacts SET number=? WHERE name=?",(number,name))
            contacts.commit()
            print("Their number has been changed.\n")

        change=yes_no("\nDo you want to change their email? (y/n) ")
        if change=="y":
            email=input("Enter New Email: ")
            contacts_exec.execute("UPDATE contacts SET email=? WHERE name=?",(email,name))
            contacts.commit()
            print("Their email has been changed.\n")

        change=yes_no("\nDo you want to change their name? (y/n) ")
        if change=="y":
            new_name=input("Enter New Name: ")
            contacts_exec.execute("UPDATE contacts SET name=? WHERE name=?",(new_name,name))
            contacts.commit()
            print("Their name has been changed.\n")

    elif choice=="3":
        name = input("Enter Current Contact Name: ").lower()
        contacts_exec.execute("SELECT name FROM contacts WHERE name=?", (name,))
        valid_name = contacts_exec.fetchone()
        while valid_name == None:
            retry = yes_no("The name you gave is not in the database. DO you want to try again? ")
            if retry == "y":
                name = input("Enter Current Contact Name: ").lower()
            elif retry == "n":
                continue
            else:
                contacts_exec.execute("SELECT name FROM contacts WHERE name=?", (name,))
                valid_name = contacts_exec.fetchone()

        contacts_exec.execute("DELETE FROM contacts WHERE name=?",(name,))
        contacts.commit()

    elif choice=="4":
        name = input("Enter Current Contact Name: ").lower()
        contacts_exec.execute("SELECT name FROM contacts WHERE name=?", (name,))
        valid_name = contacts_exec.fetchone()
        while valid_name == None:
            retry = yes_no("The name you gave is not in the database. DO you want to try again? ")
            if retry == "y":
                name = input("Enter Current Contact Name: ").lower()
            elif retry == "n":
                continue
            else:
                contacts_exec.execute("SELECT name FROM contacts WHERE name=?", (name,))
                valid_name = contacts_exec.fetchone()

        contacts_exec.execute("SELECT number, email FROM contacts WHERE name=?", (name,))
        info=contacts_exec.fetchone()

        print(f"The number for {name} is {info[0]}. The email for {name} is {info[1]}\n")

print("\n\nexiting program! Thanks for using me!")