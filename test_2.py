import os
import csv

path=r"C:\Users\Josiah\OneDrive\Desktop\encrypt_log.log"
with open(path,"r") as encrypt_log:
    reader=csv.DictReader(encrypt_log)
    for row in reader:
        print(row)