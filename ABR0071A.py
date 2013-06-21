import math
n=raw_input()
a=float(n)
a+=1
x=math.fmod(a,1.5)
x-=1
print round(x*x*x-2.25*x,1)
