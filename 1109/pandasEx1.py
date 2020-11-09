'''
window 사용자 : pip install pandas

pandas를 이해하는 데 dataframe을 이해해야한다
dataFrame은 데이터 베이스의 table과 같다
'''

import pandas as pd

ko = pd.Series([92600,92400,92100,94300,92300])

print(ko) #레코드 처럼 행단위 출력

from pandas import Series, DataFrame
#시리즈와 데이터 프래임을 별도 import해서 pandas의 네임스페이스를 거치지 않고 
#사용하는 방법 : 이미 series 임포트했기에 바로 써도된다
ko = Series([100,200,300])
print(ko)


