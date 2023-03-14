def solution(x0,e):
    def f(x):
        return x**2-2 # x값에 따른 함수 값 리턴
    def df(x):
        return 2*x #x값에 따른 미분 함수 값 리턴
    i=1 # 반복 횟수
    while True: 
        x=x0-(f(x0)/df(x0)) #뉴턴메소드를 통해 x절편 구하기
        print(f"현재 {i}번 반복했고, 근사값은 {x}이고, 오차값은 {f(x)}입니다.") #반복 횟수에 따른 근사값 출력
        if abs(f(x))<e: #함수값이 엡실론보다 작으면
            break
        i+=1 # 반복횟수 갱신
        x0=x # x값 갱신


solution(2,0.00001)
