student_num=int(input("Enter the number of students: "))
student_list={}
def grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

for student in range(1,student_num+1):
    print(f"\nStudent {student}:")
    name=input("Name: ")
    score1=int(input("Enter score 1: "))
    score2=int(input("Enter score 2: "))
    score3=int(input("enter score 3: "))
    student_list[name]=round(sum([score1,score2,score3])/3,2)

print("\n-------------------")
print("Student Details:")
for student in student_list:
    print(f"Name: {student}, Average Score: {student_list[student]}, Grade: {grade(student_list[student])}")