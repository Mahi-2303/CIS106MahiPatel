x=int(input("Enter number of concert tickets :"))
if x>=25:
  price=50
elif x>10 and x<24:
  price=60
elif x>5 and x<9:
  price=70
else:
  price=75
ttl=x*price
print("Number of tickets are:",x)
print("Price per ticket is : $",price)
print("Total cost of tickets is : $",ttl)