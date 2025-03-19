import json, os

if not os.path.exists("contacts.json"):
    with open("contacts.json", "w") as contacts_file:
        json.dump({}, contacts_file)

with open("contacts.json") as contacts_file:
    contacts=json.load(contacts_file)

def valid_input(valid,prompt):
    while True:
        valid=list(map(lambda x: x.lower(),list(valid)))

        test=input(prompt).lower()
        if test in valid:
            return test
        else:
            print("\nInvalid input {}. Please enter one of the following {}.\n".format(test,valid))

def add_contact(name,number,email):
    if name in contacts:
        print("\n{} already exists.\n".format(name))
    else:
        contacts.update({name:{"number":number,"email":email}})
        with open("contacts.json","w") as contacts_file:
            json.dump(contacts,contacts_file)

def remove_contact(name):
    if name in contacts:
        del contacts[name]
        with open("contacts.json","w") as contacts_file:
            json.dump(contacts,contacts_file)
    else:
        print("\n{} doesn't exist.\n".format(name))

def update_contact(name,data):
    contacts[name].update(data)
    with open("contacts.json","w") as contacts_file:
        json.dump(contacts,contacts_file)

def get_contact(name):
    if name in contacts:
        print("\ncontacts name is {}\ncontacts number is {}\ncontacts email is {}\n".format(name,contacts[name]["number"],contacts[name]["email"]))
    else:
        print("\n{} doesn't exist.\n".format(name))

while True:
    result=valid_input("yn","Would you like to enter the contact management system? y/n: ")
    print()
    if result=="n":
        break
    result = valid_input("1234", "Options:\n1: add contact\n2: remove contact\n3: update contact information\n4: get contact information\nWhat is your choice?: ")
    print()
    name=input("What is the contacts name? ")
    if result=="1":
        number=input("What is the contacts number? ")
        email=input("What is the contacts email? ")
        add_contact(name,number,email)
    elif result=="2":
        remove_contact(name)
    elif result=="3":
        yn=valid_input("yn","Do you want to update their name? y/n: ")
        if yn=="y":
            data=contacts[name]
            del contacts[name]
            name=input("What is the new name? ")
            contacts.update({name:data})
            with open("contacts.json","w") as contacts_file:
                json.dump(contacts,contacts_file)
        data={}
        yn=valid_input("yn","Do you want to update their number? y/n: ")
        if yn=="y":
            number=input("What is the new number? ")
            data.update({"number":number})
        yn=valid_input("yn","Do you want to update their email? y/n: ")
        if yn=="y":
            email=input("What is the new email? ")
            data.update({"email":email})
        update_contact(name,data)
    else:
        get_contact(name)
    print()

print("exiting program")