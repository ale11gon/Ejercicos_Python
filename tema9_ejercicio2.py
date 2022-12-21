from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]

def sumaImpares(x):
   return reduce(lambda a,b: a + b,(filter(lambda x: x%2 != 0,x)))

print(sumaImpares(lista))
