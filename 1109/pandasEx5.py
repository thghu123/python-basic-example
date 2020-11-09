import pandas as pd
from pandas import Series, DataFrame

emp_list = [['100','마루치','PROG'],
['102','마루','PRO'],
['104','마치','PRG'],
['108','루치','ROG']] #list in list
#열이름이 없다. ex4는 json표기법으로 했었다

c_name = ['empno','ename','job']
#위 2개를 합쳐서 만들면된다
df = DataFrame(emp_list, columns = c_name)
print(df) #result

print(df.loc[1])
#index로 인자를 얻어오는 법

print(df.loc[1:3])
#어디서 어디까지 나와라

print(df.loc[[1,3]])
#따로따로 뽑아온다.

#print(df[df.empno >= 104])
#empno가 104 이상인 애들만 출력

#print(df.query('empno>=100'))

#사번이 110번 이상이고 직종이 sales인 사원을 선택하여 출력하자

#print(df[(df.empno>=100) & (df.job == 'FROG')])
#오류가 나온다.

print(df['ename']) #특정 열만 찍는다.

print(df[['ename','job']]) #2개이상은 [] 2개




print('------------------------------------')
# 사번이 110이상이고, 직종이 'SALES'인 사원을 선택하여 출력하자!
#print(df[(df.empno>=110) & (df.job == 'SALES')])

print(df.iloc[:,0:2]) #행범위 , 열범위 :는 다나온다
#열은 0-2까지 행은 전부 다 나오게했다

#이번엔 2,3번째 행만 1,2 열민 선텍선택한다
print(df.iloc[1:3 , 0:2])

#print(df.drop([0,2])) #첫번째행과 3번째 행을 삭제한다.

#열을 삭제한다.
print(df.drop(columns='empno'))

#data 그룹만들기도 할 줄 알아야 분석이 가능하다.

#print(df[df.empno >= 200])#empno가 200이상인 행들만 출력
#print(df.query('empno>=100'))
#print(df[df.empno>= 100]) #오류 나온다

#print(df[int(df['empno']>= 100)])

#TypeError: '>=' not supported between instances of 'str' and 'int'
#에러메세지
