
'''
set 자바와 같이 중복을 허용하지 않는다
set구조는 합집합 교집합 차집합을 다 할 수 있다.

'''
icecream1 = {'체리주빌레','엄마는외계인',
'쿠키앤크림','민트초코','뉴욕치즈케이크','민트초코'}

print("{} {}".format(len(icecream1),icecream1))
#순서 정해지지 않는다. 중복값은 안들어간다

#is는 주소값 비교
res = '슈팅스타' in icecream1
print(res)

res = '뉴욕치즈케이크' in icecream1 #index별로 반복문 돌릴 필요 없다
print(res)

res = '뉴욕치즈케이크' not in icecream1 
print(res)

#집합 연산자 == 논리 연산자 의미
t1 = set('12345')
t2 = set('45674')
print(t1,t2)
#한글자라는 가정하에 가능하다.

res1 = t1&t2 #2 set 모두 가지는 교집합
print(res1)

res1 = t1|t2 #2 set 모두 가지는 교집합
print(res1)

res1 = t1-t2
print(res1) #차집합을 의미한다. 중복을 빼는 것
#합집합은 더하