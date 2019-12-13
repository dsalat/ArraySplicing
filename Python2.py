

#Dirshe Salat
def main(y):
 

  if type(y) == tuple:

    def sumGen(y):


       return sum(filter(lambda i: isinstance(i, (int,float)), y))


  if type(y) == list:

    def sumGen(y):


      return sum(filter(lambda i: isinstance(i, (int,float)), y))


  if type(y) == dict:



    def sumGen(y):

      a=sum(filter(lambda i: isinstance(i, (int,float)), y.values()))


      b=sum(filter(lambda i: isinstance(i, (int,float)), y.keys()))


      return a+b

  if type(y) == float:


    def sumGen(y):

      return "You cannot sum this type!"

  if type(y) == int:

    def sumGen(y):

      return "You cannot sum this type!"


  else:

    pass

  return sumGen

sumlist = main([])

s=sumlist([1, 2, 3.2, 'w'])

print s

sumdict = main({})

d=sumdict({1:'a', 2:3, 'x':12.6})

print d

sumtup = main((5,6))

y=sumtup((1, 2, "foo", 6))

print y

sumint = main(4)

c=sumint(9)

print c

sumfloat = main(12.5)

b=sumfloat(8.9)

print b

