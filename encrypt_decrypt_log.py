import os, datetime, csv, time
from cryptography.fernet import Fernet

def valid_input(valid,prompt):
    valid=list(map(lambda x: x.lower(),list(valid)))

    test=input(prompt).lower()
    if test in valid:
        return test
    else:
        print("\nInvalid input {}. Pleas enter one of the following {}.\n".format(test,valid))

while True:
    path=input("what is the directory path? ").strip('" ')
    if not os.path.isdir(path):
        temp=os.path.join(os.getcwd(),path)
        if not os.path.isdir(temp):
            temp=os.path.join(os.path.expanduser("~"),path)
            if not os.path.isdir(temp):
                print("Invalid path to directory {}.".format(path))
                if valid_input("yn","Try again? y/n: ")=="y":
                    continue
        path=temp
    print()
    if valid_input("yn", "Path is '{}'. continue? y/n: ".format(path)) == "y":
        break
    else:
        if valid_input("yn", "Do you want to enter a different path? y/n: ") == "y":
            continue
        else:
            print("Exiting program.")
            exit()

dirname=os.path.dirname(path)
output_folder=os.path.join(dirname,"output")

if os.path.exists(output_folder):
    if os.path.isfile(output_folder):
        os.rename(output_folder,output_folder+".temp")
        os.mkdir(output_folder)
else:
    os.mkdir(output_folder)

def encrypt():
    log_file=os.path.join(dirname,"encrypt_log.log")
    exists = os.path.exists(log_file)

    with open(log_file,"a") as log:
        writer = csv.DictWriter(log, ["time", "file", "file_size", "encrypted_file", "encrypted_file_size", "key", "rate"])
        if not exists:
            writer.writeheader()

        for file_name in os.listdir(path):
            file_path=os.path.join(path,file_name)
            key = Fernet.generate_key()
            fernet = Fernet(key)
            with open(file_path, "rb") as file:
                new_file_name=file_name + ".encrypted"
                new_file_path=os.path.join(output_folder,new_file_name)
                with open(new_file_path,"wb") as new_file:
                    read=file.read(4096)
                    while read:
                        encrypted = fernet.encrypt(read)
                        new_file.write(encrypted)
                        read=file.read(4096)

            current=time.time()
            writer.writerow({"time":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"file":file_name,"file_size":os.path.getsize(file_path),"encrypted_file":new_file_name,"encrypted_file_size":os.path.getsize(new_file_path),"key":key,"rate":os.path.getsize(file_path)/(current-os.path.getctime(new_file_path))})

def decrypt():
    log_file = os.path.join(dirname, "encrypt_log.log")
    decrypt_log_file=os.path.join(dirname,"decrypt_log.log")
    if not os.path.exists(log_file):
        print("No log file found. Exiting program.")
        exit()

    exists=os.path.exists(decrypt_log_file)
    with open(decrypt_log_file,"a") as log:
        writer=csv.DictWriter(log,["time","file","rate"])
        if not exists:
            writer.writeheader()
        with open(log_file,"r") as log_in:
            reader=csv.DictReader(log_in)
            files=os.listdir(path)
            for row in reader:
                if row["encrypted_file"] in files:
                    fernet = Fernet(eval(row["key"]))
                    encrypted_file_path=os.path.join(output_folder,row["encrypted_file"])
                    file_path=os.path.join(output_folder,row["file"])

                    with open(encrypted_file_path,"rb") as encrypted_file:
                        with open(file_path,"wb") as file:
                            encrypted_data=encrypted_file.read(4096)
                            while len(encrypted_data)>0:
                                decrypted=fernet.decrypt(encrypted_data)
                                file.write(decrypted)
                                encrypted_data=encrypted_file.read(4096)

                    current=time.time()
                    writer.writerow({"time":datetime.datetime.now(),"file":row["file"],"rate":os.path.getsize(encrypted_file_path)/(current-os.path.getctime(file_path))})

def analyze_logs():
    encrypt_log_file = os.path.join(dirname, "encrypt_log.log")
    decrypt_log_file = os.path.join(dirname, "decrypt_log.log")
    if not os.path.exists(encrypt_log_file):
        print("No encrypt log file found.")
    else:
        with open(encrypt_log_file,"r") as encrypt_log:
            reader=csv.DictReader(encrypt_log)
            total=0
            rate=0
            size_reduction=0
            for row in reader:
                total+=1
                rate+=float(row["rate"])
                size_reduction+=int(row["file_size"])-int(row["encrypted_file_size"])
        if total==0:
            print("no information found in encrypt log.")
        else:
            print(f"Total files encrypted: {total}, size reduction: {size_reduction}, encryption rate: {rate/total:.2f}Bps")
    if not os.path.exists(decrypt_log_file):
        print("No decrypt log file found.")
    else:
        with open(decrypt_log_file,"r") as decrypt_log:
            reader=csv.DictReader(decrypt_log)
            total=0
            rate=0
            for row in reader:
                total+=1
                rate+=float(row["rate"])
            if total == 0:
                print("no information found in decrypt log.")
            else:
                print(f"Decryption rate {rate/total:.2f}Bps")

print()
option=valid_input("123","Options:\n1: encrypt files in folder.\n2: decrypt files in folder.\n3: analyze logs\nWhat is your choice?: ")
print()
if option=="1":
    encrypt()
    print("Encryption completed, ",end="")
    analyze=valid_input("yn", "Would you like to analyze logs? y/n: ")
    if analyze=="y":
        analyze_logs()
elif option=="2":
    decrypt()
    print("Decryption completed, ", end="")
    analyze = valid_input("yn", "Would you like to analyze logs? y/n: ")
    if analyze == "y":
        analyze_logs()
else:
    analyze_logs()