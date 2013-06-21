a,b,c=raw_input().split()
x=float(a)
y=float(b)
z=float(c)
sum=x+y+z
urj=x*y*z
if sum>urj:
   print round(sum,1)
else:
    print round(urj,1)

