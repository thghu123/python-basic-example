import pandas as pd
from pandas import Series, DataFrame

emp_list = [{'empno':100, 'name':'나루토', 'job':'DEV'},
{'empno':120, 'name':'사스케', 'job':'DEV'},
{'empno':210, 'name':'이타치', 'job':'DEV'}]

#json과 유사하고, 이런 형태로 많이 추출한다
df = DataFrame(emp_list)
#make(transform) dataFrame
print(df) #key = column

print("---")
df = df[['empno','job','name']] #컬럼 순서 변경하기 
print(df)
