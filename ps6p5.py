x=input("Enter last name of employee :")
y=int(input("Enter salary of employee :"))
z=int(input("Enter job level of employee :"))
if z>=10:
  rate=(25/z)*100
elif z>5 or z<9:
  rate=(20/z)*100
else:
  rate=(10/z)*100
print(rate)
bonus=y*rate
print("Last name of employee is :",x)
print("Bonus employee gets is :",bonus)