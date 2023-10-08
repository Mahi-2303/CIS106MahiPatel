count = 0
x= input("Do you want to run this program? (Yes/No): ")
while True:   
    if x!= "yes":
        break
    lname = input("Enter the student's last name: ")
    e1 = float(input("Enter the exam1 score: "))
    e2 = float(input("Enter the exam2 score: "))  
    ave= (e1+e2) / 2
    print("Student's last name is :", lname)
    print("Average exam score is :", ave)
    count += 1
    y=input("Do you want to enter data for another student? (Yes/No): ")
    if y != "yes":
        break
print("Total number of students entered:", count)