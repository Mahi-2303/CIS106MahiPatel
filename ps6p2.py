x=input("Enter a part number :")
y=int(input("Enter quantity :"))
if x==10 or x==55 or x=="10" or x=="55":
  cost=1.00
elif x==99 or x=="99":
  cost=2.00
elif x==80 or x==70 or x=="80" or x=="70":
  cost=3.00
else:
  cost=5.00
ttl=y*cost
print("Part number is :",x)
print("Cost per unit is : $", cost)
print("Total cost is : $",ttl)