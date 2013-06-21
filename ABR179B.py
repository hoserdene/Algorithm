n=input()
a=raw_input()
mas=[]
mas=a.split()
count=0
for x in xrange(0,n):
  if int(mas[x])%7==1 or int(mas[x])%7==2 or int(mas[x])%7==5:
     count+=1
print count
