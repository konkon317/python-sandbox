array0 = range(10) #連番でリストを作る
print(array0)
for item in array0 :
 print(item)
print()

array0 = range(10,-10,-3)#連番でリストを作る 開始　終了 間隔を指定
print (array0) 
for item in array0 :
 print(item)
print()

array0 = list("あいうえお") #文字列から作成 
print (array0) 
for item in array0 :
 print(item)

index =array0.index('あ')       #指定した要素が何番目かを調べる
print("\'あ\' は",index,"番目") #同じあたいが複数あるなら最初に見つかった場所が返る　→　範囲指定もできるので最初以外も大丈夫
index =array0.index('う')
print("\'う\' は",index,"番目")

#index =array0.index('か')       リスト中にないものを探そうとしたらエラーが起きる
#print("\'か\' は",index,"番目")

print()

array0 = list((0,1,2)) #タプルから作成 
print (array0) 
for item in array0 :
 print(item)
print()

array0=list((0,0,0,0,5,3,2,1))
count = array0.count(0)      #リスト中に何個 0があるかを数える
length =len(array0)          #要素数を数える
print(array0,"の中に0が",count,"個")
print(array0,"の要素数は",length,"個")