class myclass :
    def __init__(self): #생성자
        self.name ='' #초기화 : 오류 방지

    def __del__(self): #소멸자 - 객체가 메모리 상에서 삭제될 때 호출
        #할일 있을 때 쓰자.
        self.name =''

        
    def setName(self, n): #멤버 메서드 정의
        self.name = n #self는 this, 초기화 부
    #멤버 메서드 정의시 반도시 첫번째 인자는 현 객체의 레퍼런스인 self 넣어준다

    def getName(self):
        return self.name
    