x=[1,2,3]
print ('x=[1,2,3]')
print('x type is ',type(x))
print(x)
print(x[0])
print()

x=set([1,2,3])			#重複を許さない集合
print ('x=set([1,2,3])')
print('x type is ',type(x))
print(x)
print()


x=frozenset([1,2,3])           #変更不可セット
print ('x=frozenset([1,2,3])')
print('x type is ',type(x))
print(x)
print()

x={1,2,3,4}
print ('x={1,2,3,4}')
print('x type is ',type(x))
print(x)
print()

x={'a':1,'c':6}
print ('x={\'a\':1,\'c\':6}')
print('x type is ',type(x))
print(x)
print(x['c'])
print()