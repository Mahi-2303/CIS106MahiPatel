def bowler(s1,s2,s3,handicap):
  sum=s1+s2+s3
  avg=sum/3
  havg=(sum+handicap)/3
  return avg,havg

lname=input("Enteryour last name :")
s1=float(input("Enter score 1 :"))
s2=float(input("Enter score 2 :"))
s3=float(input("Enter score 3 :"))
handicap=float(input("Enter handicap :"))
avg,havg=bowler(s1,s2,s3,handicap)
print("Bowler's last name is :", lname)
print("Average score :",avg)
print("Handicap average :",havg)
