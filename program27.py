n=float()
str = 'a123'
#str = '123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('Not numeric')
print()
