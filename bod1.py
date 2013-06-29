import random
a=raw_input()
mas=[]
mas=a.split()
n = len(mas)
for x in xrange(n):
   y = random.randint(0, len(mas)-1)
   print mas[y]
   del mas[y]
