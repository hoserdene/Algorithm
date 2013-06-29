n=input()
mas=[]
for i in xrange(0,n):
  for j in xrange(0,n):
     a=float(1)
     b=float(i+j)
     sum=a+b
     mas[i][j]=sum
     print round(float(max[i][j]),2)
