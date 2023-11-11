def report(sales):
  if sales>100000.00:
    per=0.10
  elif sales<=100000.00:
    per=0.05
  comm=sales*per
  nxtyr=sales*1.05
  return comm,nxtyr
  
person=input("Enter name of sales person :")
lname=input("Enter lastname ")
sales=float(input("Enter sales amount :"))
comm,nxtyr=report(sales)

print("Name of salesperson is :" , person)
print("Last name of sales person is :",lname)
print("Sales amount is :",sales)
print("Commission is :",comm)
print("Next year sales is :",nxtyr)