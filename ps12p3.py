def hilow(lname,score):
  l=len(lname)
  high=-1.0
  low=99999999.99
  hiindex=0
  loindex=0
  for y in range(0,l,1):
    if float(score[y])>float(high):
      high=score[y]
      hiindex=y
    if float(score[y])<float(low):
      low=score[y]
      loindex=y
  print("Highest score is ",lname[hiindex],score[hiindex])
  print("Lowest score is ",lname[loindex],score[loindex])

lname=("patel","shah","limbachiya","thakkar","jain","agrawal","damani","amrutiya","parmar","katara")
score=("100","49","90","86","78","67","56","45","34","23")
hilow(lname,score)