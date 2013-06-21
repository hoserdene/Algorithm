n=input()
a=n
b=1
while a>9:
	a=a/10
	b=b*10
c=n%10
n=n/10
n=n*10
n=n+a
n=n%b
n=c*b+n
print n
