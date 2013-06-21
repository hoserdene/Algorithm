x,y,z,w=raw_input().split()
a=int(x)
b=int(y)
r=int(z)
s=int(w)
if a%b==r:
  print 'R'
if a%b==s:
  print 'S'
if a%b!=r and a%b!=s:
  print 'No solution'

