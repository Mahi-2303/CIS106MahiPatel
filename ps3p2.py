x = int(input("Enter purchase price per share :"))
y = int(input("Enter current stock price :"))
z = int(input("Enetr quantity of stock :"))
a = y - x
print("Value of stock is :", a)
if a > 0:
  print(" You are in profit")
else:
  print("You are losing money")
