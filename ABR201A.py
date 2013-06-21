n=input()
a=raw_input()
mas=[]
mas=a.split()
max=float(mas[0])
for x in xrange(1,n):
   if max<float(mas[x]):
      max=float(mas[x])
print round(max,1)
