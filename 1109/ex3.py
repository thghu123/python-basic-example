import os

cpath = os.getcwd()
print("현재위치",cpath)

#현재 파일이 위치하고 있는 폴더내 모든 파일을 얻어내자
sub_list = os.listdir(cpath)
print(sub_list)



