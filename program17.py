n=int(input())
sum=0
temp=n
while(temp>0):
	dig=temp%10
	sum+=dig**3
	temp//=10
if n==sum:
	 print("yes")
else:
	  print("no")
