import os

cpath = os.getcwd()
print("현재위치",cpath)

#현재 파일이 위치하고 있는 폴더내 모든 파일을 얻어내자
sub_list = os.listdir(cpath)
print(sub_list)




#1부터 45까지의 난수를 6개만 발생시켜 출력하는 예문을 작성
set = {}
