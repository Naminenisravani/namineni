c,d=map(int,raw_input().split())
for i in range(c+1,d):
	if i>1:
		for j in range(2,i):
			if(i%j==0):
				break
			else:
				print i,
