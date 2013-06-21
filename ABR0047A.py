a,b,c=raw_input().split()
x=float(a)
y=float(b)
z=float(c)
if x<y+z and y<x+z and z<x+y:
  print 'YES'
else:
  print 'NO'
