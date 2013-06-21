a,b=raw_input().split()
x=float(a)
y=float(b)
if x>y:
  print round(x-y,1)
else:
  print round(y-x+1,1)
