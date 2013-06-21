a,b=raw_input().split()
k=int(a)
i=int(b)
if k!=i:
   if k>i:
      i=k
      print int(k),int(k)
   else:
      print int(i),int(i)
else:
   print int(0),int(0)
