def is_odd(n):
   "Ugugdsun too sondgoi esehiig shalgah function"
   '''Jishee ni: 
          3 bol True
        100 bol False
      utga butsaana ''' 
   if n%2!=0:
     return True
   else:
     return False
print is_odd(3)
print is_odd(100)
#if __name__=="__main__":   
print type(is_odd)
print is_odd.__name__
print is_odd.__doc__

a=[0,1,2,3]
b=[a**2 for a in range(10)]
print b
