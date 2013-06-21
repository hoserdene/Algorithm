n=input()
a=raw_input()
mas=[]
mas=a.split()
sum=0
for x in xrange(0,n):
   sum+=float(mas[x])
print round(sum,1)
