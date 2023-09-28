x=int(input("Enter quantity of widgets : "))
if x>10000:
  price=10
elif x>5000 and x<10000:
  price=20
else:
  price=30
ext=x*price
print("Extended price of widgets is : $",ext)
tax=(ext/7)*100
print("Tax amount is : $",tax)
total=ext+tax
print("Total amount is : $",total)