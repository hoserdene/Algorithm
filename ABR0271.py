import math
a=raw_input()
mas=[]
mas=a.split()
sum=0
count=0
for x in xrange(0,len(mas)):
   sum+=int(mas[x])
   count+=1
dundaj=sum/float(count)
print round(dundaj,1)
sum2=0
for x in xrange(0,len(mas)):
   z=int(mas[x])-int(dundaj)
   sum2+=z*z
y=1/float(count)
print round(math.sqrt(float(y)*sum2),1)
