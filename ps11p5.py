ttl=0
tax=0
def compttl(qty,price):
  global ttl
  ttl=qty*price
  global tax
  tax=ttl*0.07
  return ttl

qty=int(input("Enter quantity of iteam :"))
price=int(input("Enter price pf item :"))
compttl(qty,price)
print("Your total is :$",ttl)
print("Tax cost is :$ ",tax)