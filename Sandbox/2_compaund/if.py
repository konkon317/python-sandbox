
x=0
y=0
z=0

if x==0 :
    y=33
    print('true')
    print(y)

else :
    z=2
    print('false')
    print(z)

print ('end')
print()

#print (z) #//tureの場合は変数が作られないのでエラー
#print (y) #//falseの場合は変数が作られないのでエラー
#c++のようなブロックのスコープはないっぽい


for i in range(4):
    print("i : ",i)    

    if i==0 :
        print("i==0")
    elif i==1:
        print("i==1")
    else :
        print("other")
    
    print()

print("end_2")