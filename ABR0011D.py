import math
q,w,e=raw_input().split()
x=float(q)
y=float(w)
z=float(e)
a=(2*math.cos(x-3.14/6))/(1/float(2)+math.sin(y)*math.sin(y))
b=1+(z*z)/(3+z*z/5)
print round(a,3), '%.3f' % b
