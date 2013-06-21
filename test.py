a=raw_input()
x=float(a)
n=x
z=0
if x>0:
    while x>=1:
        x-=1
        z+=1
    if x<=0.5:
        y=n-x
    else:
        y=n-x+1
    print int(z)
    print int(y)
    print int(z)
else:
    while x<=0:
        x=x+1
        z-=1
    if x<=0.5:
        y=n-x
    else:
        y=n-x+1
    print int(z)
    print int(y)
    print int(z)+1
        
