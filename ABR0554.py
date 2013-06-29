n=input()
for a in xrange(1,n/2):
  for b in xrange(a+1,n/2):
   for c in xrange(b+1,n/2):
     if a*a+b*b==c*c and a<=b and b<=c and c<=n/2:
       print a,b,c 
