#key와 value가 한쌍이 되어서 들어가는 dict == map in java

d1 = {'k1':100, 2:'안녕디지몬'}
#키가 반드시 문자열이 아니여도 된다
print(d1)

d1[3] = 100 #추가
d1[2] = 200 #수정
#보통 [ ]은 인덱스로 보이는 데 key값이다.
print(d1)

del d1[2] #키가 2인 요소를 삭제한다
print(d1)

#java에서는 put, get
v1 = d1.get('k1')
print(v1)
#이렇게 가져올 수 있다.

#dic에 있는 저장된 모든 key 얻어내기
keys = d1.keys()
print(keys)
print(type(keys))#dict_keys라는 자료형 

values = d1.values()
print(values)
print(type(values))

#중요
#dict_keys라는 자료형 - 배열 아님 - 변환
key_list = list(keys) #주소 복사 안되게 list( )를 써줘야한다
print(key_list)

v2 = d1.get(3)
print(v2)

v2 = d1.get('ky2','no value') #key가 없을 때 뒤의 값이 나온다
print(v2)

d1.clear() #내부를 비운다. 
print(d1)

var1 = 100
var2 = 200
var3 = var1 #주소 복사 True
chk = var1 is var3
print(chk)

print(id(var1))
print(id(var3)) #id값가져올 수 있다.

var3 = 200
print(var1)

var1 = 400
chk = var1 is var3
print(chk) #False

print(id(var1))
print(id(var2))
