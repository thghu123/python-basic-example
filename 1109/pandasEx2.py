from pandas import Series, DataFrame

ko = Series([100,200,300,400,500], index = ['11-01','11-02','11-03','11-04','11-05'])

print(ko)
#index로 나오는 게 아닌 key값처럼 index[] 가 나온다
print("-------------------------------------------")

for date in ko.index:
    #index find
    print(date)

print("-------------------------------------------")
for price in ko.values:
    print(price)

print("-------------------------------------------")
ko2 = Series([400,950,200], index=['11-01','11-02','11-03'])

sum = ko + ko2 #안의 index가 같으면 +연산이 가능하다.

ko.append(ko2) #2개가 합쳐진다.
print(ko)