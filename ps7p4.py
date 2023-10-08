gross=0
count=0
ttl=0

while True:
    x=input("Do you want to continue? (Yes/No): ") 
    if x!="yes":
        break
    lname=input("Enter employee last name: ")
    hrs=float(input("Enter hours worked: "))
    pay=float(input("Enter rate of pay: "))
    
    if hrs>40:
        gross=(40 * pay) + ((hrs - 40) * 1.5 * pay)
    else:
        gross = hrs * pay
    
    print("Employee last name:",lname)
    print("Gross pay:",gross)
    
    ttl += gross
    count += 1
    
    y = input("Do you want to enter data for another employee? (Yes/No): ")
    
    if y!="yes":
        break
print("Total number of data is :",count)

if count > 0:
    ave = ttl / count
    print("Total gross pay: ",ttl)
    print("Number of employees:",count)
    print("Average pay:",ave)
else:
    print("No employee data entered.")





