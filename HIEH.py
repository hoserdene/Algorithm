a,b=raw_input().split()
while int(a)!=int(b):
    if int(a)>int(b):
        a=int(a)-int(b)
    else:
        b=int(b)-int(a)
print int(a)
