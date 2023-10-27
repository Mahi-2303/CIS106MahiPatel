def fcst(month):
  if month in ['Jan','Feb','Mar']:
    return 0.10
  elif month in ['Apr','May', 'Jun']:
    return 0.15
  elif month in ['Jul','Aug','Sep']:
    return 0.20
  else:
    return 0.25
def nxtsal(month,sales):
  per=fcst(month)
  nxtsal=sales*(1+per)
  return nxtsal
while True:
  cont=input("Do you want to do the program(yes/no)")
  if cont!="yes":
    break
  lname=input("Enter your last name :")
  month=input("Enter the month :")
  sales=int(input("Enter your sales :"))
  per=fcst(month)
  nxt=nxtsal(month,sales)
  print("Your sales are :",sales)
  print("Your forecast percent  is :",fcst(month))
  print("Your next salary is :",nxtsal(month,sales))

    
  