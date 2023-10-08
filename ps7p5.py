ttl_dis=0
while True:
  x=input("Do you want to continue this program (Yes/No)?")
  if x!="yes":
    break
    
  qty=int(input("Enter quantity of an item :"))
  price=float(input("Enter price of an item :"))
  ext=qty*price
  if ext>10000.00:
    dis=0.25
  else:
    dis=0.10
  amt=ext*dis
  ttl=ext-amt
  ttl_dis+=1
  print("Extended price of item is :",ext)
  print("Discounted percent of item is :",dis)
  print("Discounted amount of item is :",amt)
  print("Total price of an item is :",ttl)
  y=input("Do you want to enter another order (Yes/No)? :")
  if y!="yes":
    break
  print("Total discount is :",ttl_dis)