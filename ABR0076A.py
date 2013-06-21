a,b,c,d=raw_input().split()
k=int(a)
l=int(b)
m=int(c)
n=int(d)
if ((k+l)%2==0)-((m+n)%2!=0):
   print 'YES'
else:
   print 'NO'
