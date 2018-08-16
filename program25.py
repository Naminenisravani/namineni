def median(l,n):
  l.sort()
  if n%2==0:
    return l[n/2]
  else:
    return (l[n/2-1]+l[n/2])/2
  n=int(raw_input())
  l=[int(a) for a in raw_input ().split()]
  print(median(l,n-1))
