def outdoor(make,model,evcode,msrp):
  if make=="Honda" and model=="Accord":
    peroff=0.1
  elif make=="Toyota" and model=="Rav4":
    peroff=0.15
  elif evcode=="Y":
    peroff=0.30
  else:
    peroff=0.05
  dis=peroff*msrp
  new=msrp-dis
  ttl=new+(0.07*new)
  return ttl
ttlmsrp=0.0
ttlsales=0.0
while True:
  cont=input("Enter do you want to continue (Yes/No): ")
  if cont!="yes":
    break
  make=input("Enter make of car:")
  model=input("Enter model of car :")
  evcode=input("Enter ev code of car:")
  msrp=float(input("Enter msrp of the car:"))
  outdoorprice=outdoor(make,model,evcode,msrp)
  print("Out door price is :",outdoorprice)
  ttlmsrp=ttlmsrp+msrp
  ttlsales=ttlsales+outdoorprice
    
print("Sum of total msrp of car is :",ttlmsrp)
print("Sum of sales of all price is :",ttlsales)