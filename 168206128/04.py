   def sum (alist, L=[]):
       if len(L)==0:
           L.append(0)
       if len(alist) != 0:
           L[0]+=alist[0]
           alist.remove(alist[0])
           return sum(alist)
       return L[0]
   alist = [4,1,7,2]
   s=sum(alist)
   print(s)
