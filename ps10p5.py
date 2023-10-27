def assesval(county,mktval):
  if county=="Cook":
    val=0.90
  elif county=="Dupage":
    val=0.80
  elif county=="McHenry":
    val=0.75
  elif county=="Kane":
    val=0.60
  else:
   val=0.70
  return val
  
ttlmkt=0
ttlval=0  
while True:
  cont=input("Enter do you want to continue tis program(yes/no)")
  if cont!="yes":
    break
  county=input("Enter the county name")
  mktval=int(input("Enter the market value"))
  val=assesval(county,mktval)
  print("The value of the property is ",val)
  ttlmkt+=mktval
  ttlsal=ttlmkt*val
  print("The total sales is ",ttlsal)
  print("The total market val is :" ,ttlmkt)