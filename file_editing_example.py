import os

#get the home directory.
home_directory = os.environ["HOMEPATH"]

#joins the home directory to cat.txt than formats the result to be readable by the system.
new_file=os.path.join(home_directory, "cat.txt").replace("\\","/")

#opens the file, and if there isn't a file makes it.
with open(new_file, "w+") as file:
    #writes to file
    file.write("Cats are cool!\n")
    #moves the point we are at in the file to 0
    file.seek(0)
    #get content from file
    file_content=file.read()
    #print content
    print(file_content)

#removes the file
os.remove(new_file)
