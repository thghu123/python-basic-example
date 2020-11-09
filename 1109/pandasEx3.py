'''
test_data.tsv 파일 생성 - 값을 채우고 가져오자
col1	col2	col3
120	210	2018
220	210	2019
136	230	2020
'''
import pandas as pd

df = pd.read_csv('1109/test_data.tsv',sep = '\t')
# 'data/test_data.tsv' in eclipse ex
# 현 python folder 기준으로 경로 입력
# 열의 구분자는 tab

print(df) 

print('-----------------------------------------------')
print(df.tail(2)) #행 2개만
print('-----------------------------------------------')
print(df.col2) #열 하나만

