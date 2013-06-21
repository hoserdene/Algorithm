a,b,c=raw_input().split()
x=float(a)
y=float(b)
z=float(c)
if x>y>z:
   print round(x,1)
else :
    if y>z:
        print round(y,1)
    else:
        print round(z,1)
