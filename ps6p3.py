x=int(input("Enter principle amount of CD :"))
y=int(input("Enter year to maturity of CD :"))
if x>100000 and y==5:
  int=(6/x)*100
elif x>50000 and x<100000 and y==10:
  int=(5/x)*100
elif x>50000 and x<100000 and y==5:
  int=(4/x)*100
else:
  int=(2/x)*100
fyint=x*int
print("Principle amount of CD is : $",x)
print("Interest rate is : $",int)
print("Interest amount for first year is : $",fyint)