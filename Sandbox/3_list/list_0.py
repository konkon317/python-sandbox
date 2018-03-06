
array  = [1,2,3,4]

print(array)

array[0] *= 10

print(array)

array2 = array[0:2] #範囲読み出し

print(array2)

array[0:2] = [array2[0]*10 , array2[1]*10] #範囲代入
print(array)

array.append(1000) #末尾に追加　push_back
print(array) 


array.append("文字列") #末尾に追加　型が他と異なっても大丈夫
print(array) 

array.append(array2) #別のリストを要素として持てる 
print(array)

print(array[6][0])#リスト中のリストはc++などでの多次元配列と同じ感じでアクセス

array2[0]="test" 
print(array2)
print(array) #参照でつながっているので　array2が変更されると arrayの要素の方も変わる

x = "test2"  
array.append(x)
print(array)
x="test3"    #ここではxを変更してもarray側は変わらない　オブジェクト型によって参照でつながる場合と単純コピーの場合があるらしい
print(array)

print()
for item in array:
    print(item)

print()

print("test2" in array) #指定した値の要素を持つかを調べる
print("test" in array)
