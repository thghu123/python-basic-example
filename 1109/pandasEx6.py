import pandas as pd
from pandas import Series, DataFrame

emp_list = [
    {'empno':100, 'name':'마루치','job': 'prog' },
    {'empno':120, 'name':'아라치','job': 'analysis' },
    {'empno':340, 'name':'을불','job': 'prog' },
    {'empno':310, 'name':'창조리','job': 'sales' },
    {'empno':349, 'name':'홍길동','job': 'prog' },
    {'empno':219, 'name':'마이클','job': 'sales' },
    {'empno':409, 'name':'일지매','job': 'analysis' }
]
print()
#보면 job을 가지고 group화 시킬 수 있겠다.
df = DataFrame(emp_list)
print(df)

#job을 가지고 그룹화 시킨다
group_job = df.groupby('job')
print(group_job)#알수없는 결과 - 객체 생성 시의 ID 값
print(group_job.groups) #이렇게 묶였음을 알려줌
print()

for name, group in group_job:
    print(name + ":" + str(len(group))) #group의 길이를 찍어라
    #name 값은 어떻게 prog로 들어가는 가?
    #그룹은 3개이다. 그 중 이름은 name, group 이 들어간것
    #group도 리스트이다 1,6 이렇게 2개 들어가있으니까
    print(group)  #다 출력해준다.
      