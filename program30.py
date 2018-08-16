hour1,min1=map(int,raw_input().split())
hour2,min2=map(int,raw_input().split())
t1=hour1*60+min1
t2=hour2*60+min2
diff=abs(t1-t2)
time=diff%60
time1=(diff-time)//60
print time1,time
