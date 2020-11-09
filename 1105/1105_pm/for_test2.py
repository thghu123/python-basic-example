#배열을 반복할 때 index와value를 같이 출력하기 위해
#enumerate를 사용한다

ar = ['python' , 'java bible' ,'Scipy','tensor']

for i in enumerate(ar):
    print(i)

#하나의 객체가 되서 들어갔다. 
#따로 뺐으면 좋겠따

for i,v in enumerate(ar):
    print(i)
    print(v)
#index는 i 값은 v에 들어간다.

#문제 구구단


for i in range(1,10,1): #1은 default여서 생략 가능하다.
    for j in range(2,10,1):
        print("{}x{}={}\t".format(j,i,j*i), end ='')
    print()


