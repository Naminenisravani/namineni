n=int(raw_input())
print("enter '0' for exist")
n=input("enter any character")
if n==0:
   exit();
else:
    if((n>='a' and n<='z') or (n>='A' and n<='z')):
           print("Alphabet")
    else:
           print("Not")
