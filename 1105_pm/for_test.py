'''
for 변수 in iterable :
    반복문장1
while 조건식 : 
    수행문장1

'''

ar1 = [1,2,3,4,5,6,7,8,9]
'''
for i in ar1 :
    print("\n{}단".format(i))
    for j in ar1 : 
        print("{}x{}={}".format(i,j,i*j))
        if(j>=9):
            
            break
    if(i>=9):
            break
'''

str = 'abcdefg'
for i in str :
    print(i)       

for i in ar1 :
    if(i==1):
        continue
    print("\n{}단".format(i))
    for j in ar1 : 
        print("{}x{}={}".format(i,j,i*j))

'''
정해진 회차를 반복할 때 range를 많이 쓴다.
구성
    range(begin,end+1,increment)
'''
for i in range(0,8,1):
    print(ar1[i])