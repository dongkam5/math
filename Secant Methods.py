#Secant Methods
import math
def secantmethod(x0,x1,e):   
    def f(x):
        return 2*(x**2) + 5 - math.exp(x) # x값에 따른 함수 값 리턴
    i=1 # 반복 횟수
    imax = 101
    while i<imax:
        x2=x1-f(x1)*((x0-x1)/(f(x0)-f(x1)))#secant메소드를 통해 x절편 구하기
        print(f"현재 {i}번 반복했고, 근사값은 {x2}이고, 오차값은 {abs(x2-x1)}입니다.") #반복 횟수에 따른 근사값 출력
        if abs(x2-x1)<e: #오차값이 입실론보다 작으면 탈출
            break
        i+=1 # 반복횟수 갱신
        x0=x1
        x1=x2 # x값 갱신

x0 = input("초기값 x0을 입력하세요(3 =< x0 =< 4): ")
x1 = input("초기값 x1을 입력하세요(3 =< x0 =< 4): ")
e = input("오차값 e를 입력하세요: ")
secantmethod(float(x0), float(x1), float(e)) #input으로 입력받은 값들은 문자열이므로 float형태로 변환
