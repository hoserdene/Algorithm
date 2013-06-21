import math
a,b,c=raw_input().split()
x=float(a)
y=float(b)
z=float(c)
print round(y+x/(y*y+abs(x*x/(y+x*x*x/3))),1)
zereg=math.tan(z/2)
print round(1+zereg*zereg,1)
