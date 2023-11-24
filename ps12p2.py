def disname(l_names,score):
  l=len(l_names)
  print("Arrays in order are :")
  for i in range (0,l,1):
    print(l_names[i],score[i])
def reverse(l_names,score):
  l=len(l_names)
  print("=========================================")
  print("Arays in reverse order are :")
  for j in range (l-1,-1,-1):
    print(l_names[j],score[j])
l_names=("patel","shah","limbachiya","thakkar","jain","agrawal","damani","amrutiya","parmar","katara")
score=("100","49","90","86","78","67","56","45","34","23")
disname(l_names,score)
reverse(l_names,score)