def footage(len,wid,hgt):
  foot=(2*len*wid)+(2*len*hgt)+(2*wid*hgt)
  return foot
  
def gallons_needed(foot):
  gallons=foot/50
  return gallons

while True:
  cont=input("Do you want to continue this program?(yes/no)")
  if cont!="yes":
    break
  else:
    len=int(input("Enter lenght of the room :"))
    wid=int(input("Enter width of the room :"))
    hgt=int(input("Enter height of the room :"))
    foot=(2*len*wid)+(2*len*hgt)+(2*wid*hgt)
    gallons=foot/50
    print("Square footage of the room is :",foot)
    print("Gallons needed for paint is :",gallons)