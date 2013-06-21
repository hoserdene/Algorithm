n=input()
u=[]
u.insert(0,0)
u.insert(1,1)
i=2
for y in xrange(2,n+1):
  u.insert(i,u[y-1]+u[y-2])
  i+=1
for y in xrange(0,n+1):
  print u[y]
