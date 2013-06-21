n=input()
a=raw_input()
mas=[]
mas=a.split()
urj=1
for x in xrange(0,n):
    urj=urj*float(mas[x])
print round(urj,1)
