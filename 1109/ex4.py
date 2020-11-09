import random

#r = range(1,11) #1부터 10까지 범위
#dice = random.choice(r)
#print(dice)

s = set() #중복 제외
r = range(1,7)
#1부터 45까지의 난수를 6개만 발생시켜 출력하는 예문을 작성

for i in range(20): #whle 무한히 돌리고 break해도된다.
    s_len = len(s)

    s.add(random.choice(r))
    if len(s) == 6 :
        break

print(s)