f=open("employee.txt","r")
ttl=0.0
lname=str(f.readline().rstrip('\n'))
while lname!="":
  sal=float(f.readline())
  if sal>=100000:
    bonus=sal*2
  elif sal>=50000:
    bonus=sal*.15
  else:
    bonus=sal *.10
  print("Employee : ", lname)
  print("Salary : ", sal)
  print("Bonus : ", bonus)
  print(" ")
  ttl+=bonus
  lname=str(f.readline().rstrip('\n'))
f.close()

print("Total amount of bonuses given is :", ttl)