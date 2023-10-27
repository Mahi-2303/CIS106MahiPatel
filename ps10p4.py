def ticket(lname,miles):
  if miles>30:
    price=12
  elif miles>20 and miles<29:
    price=10
  elif miles>10 and miles>19:
    price=8
  else:
    price=5
  return price

ttl=0
while True:
  cont=input("Enter do you want to continue this program(yes/no)")
  if cont!="yes":
    break
  lname=input("Enter last name :")
  miles=int(input("Enter miles from downtown Chicago :"))
  price=ticket(lname,miles)
  print("The price of ticket for",lname,"is",price)
  ttl+=price
print("Total price of tickets is",ttl)