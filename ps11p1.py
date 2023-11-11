def calcdisc(qty,price,discrate):
  total=qty*price
  discamt=total*discrate
  discprice=total-discamt
  return discamt,discprice

def main():
  qty= int(input("Enter quatity of item: "))
  discrate=float(input("Enter discount rate : "))
  price=float(input("Enter price of item: $ "))
  discamt,discprice=calcdisc(qty,price,discrate)
  print("Quantity you enetred is :",qty)
  print("Price you entered is $ :",price)
  print("Discount amount: $ ",discamt)
  print("Discounted price: $ ",discprice)

main()