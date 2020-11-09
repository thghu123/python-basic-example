import pandas as pd
from pandas import Series, DataFrame

emp_list = [
    {'empno':100, 'name':'마루치','job': 'prog' },
    {'empno':120, 'name':'아라치','job': 'analysis' },
    {'empno':340, 'name':'을불','job': 'prog' },
    {'empno':310, 'name':'창조리','job': 'sales' },
    {'empno':340, 'name':'을불','job': 'prog' },
    {'empno':349, 'name':'홍길동','job': 'prog' },
    {'empno':219, 'name':'마이클','job': 'sales' },
    {'empno':409, 'name':'일지매','job': 'analysis' },
     {'empno':100, 'name':'마루치','job': 'prog' }
]

df = DataFrame(emp_list)
print(df)

print('-----------------------------------------------')
#중복되는 값 모두 출력한다

#중복 체크
print(df.duplicated('name')) #중복시 True 아닐 시 false

print(df.drop_duplicates()) #중복값이 사라진다.


