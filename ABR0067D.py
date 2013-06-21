n=input()
count=0
while n>0:
   a=n%10
   count+=1
   if count==2:
      print a
   n/=10
