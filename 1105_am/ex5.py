#튜플은 불변 읽기 전용
#자바에서는 배열의 크기는 조절할 수 없었다. 더 나아가 값도 못바꾸는 게
list1 = [1,2,3,4,5]
tuple = (200,1,2,3,4)
#수정 불가
print(tuple.index(1))

list2 = list1[:] #내용 복사
#그냥 [:]없이도 들어가고 옵션으로 들어간다.

print(list2)
chk = list2 is list1 #주소비교 false
print(chk)

list2 = list1 #주소 복사
chk = list2 is list1 #주소비교 True
print(chk)

list2[2] = 1
print(list1)
#memory sharing? True