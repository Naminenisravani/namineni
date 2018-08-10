n,r=map(int,raw_input().split())
for num in range(n,r):
     sum=0
     temp=num
     while temp>0:
           digit=temp%10
           sum+=digit**3
           temp //=0
     if num == sum:
           print(num)
