n=input()
p=n
sum=0
while n>0:
   a=n%10
   sum+=a*a*a
   n/=10
if sum==p*p:
  print 'YES'
else:
  print 'NO'
