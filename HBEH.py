n,m=raw_input().split()
urj=int(n)*int(m)
while int(n)!=int(m):
    if int(n)>int(m):
        n=int(n)-int(m)
    else :
        m=int(m)-int(n)
print urj/int(m)
