def disname(l_names):
  l=len(l_names)
  print("Arrays in order are :")
  for i in range (0,l,1):
    print(l_names[i])
def reverse(l_names):
  l=len(l_names)
  print("Arays in reverse order are :")
  for j in range (l-1,-1,-1):
    print(l_names[j])
l_names=("patel","shah","limbachiya","thakkar","jain","agrawal","damani","amrutiya","parmar","katara")
disname(l_names)
reverse(l_names)