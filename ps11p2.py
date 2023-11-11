def student(e1,e2,e3):
  sum=e1+e2+e3
  ttl=300
  per=(sum/ttl)*100
  avg=sum/3
  points=e1+e2+e3
  return points,avg

lname=input("Enter last mane of student :")
e1=int(input("Enter exam 1 score: "))
e2=int(input("Enter exam 2 score: "))
e3=int(input("Enter exam 3 score: "))
points,avg=student(e1,e2,e3)
print("Last name of student is :" ,lname)
print("Total score of all exam is : ",points)
print("Average score of total of all exam is : ",avg)