import math
r,n=raw_input().split()
rad=float(r)
onts=int(n)
print round(onts*math.sqrt(2*rad*rad-2*rad*rad*math.cos(2*3.14/onts)),1)

