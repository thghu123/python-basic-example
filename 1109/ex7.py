fs = open("ex1.py",'r',encoding='utf-8')
#read라는 의미

#mode : r읽기 w쓰기 a추가 rb바이너리로 읽기

content = fs.read()
fs.close()
print(content)
print('==============================')
fs = open("ex1.py",'r',encoding='utf-8') 
#에러 , 해당 파일내로 접근 시 인식하여 읽기 가능
while True:
    content = fs.readline()
    if(content != ''):
        print(content, end ='') #화면 출력 후 마지막 엔터 공백으로 제거 
    else : 
        break

fs.close()
print('파일의 끝')
