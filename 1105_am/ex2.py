#비교 연산자

#주어지는 여러개의 조건의 결과로 논리적인 결과를 만든다
a = 27
b = 19
print("a={}, b={}".format(a,b))

print((a>b) & (a>=30))
print((a>b) | (a>=30))
a+=1
print(a)

#++, -- 와 같은 증감 연산자는 지원하지 않는다.
#굳이 하려면 a+=1과 같은 식을 사용해야하는 데 이것 또한 
#프린트 함수 내에서 사용하지 못한다