n=input()
a=raw_input()
mas=[]
mas=a.split()
count=0
for x in xrange(0,n):
  if int(mas[x])>=2:
     if int(mas[x])/2%2!=0:
        count+=1
print count 
