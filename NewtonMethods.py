from sympy import symbols,Derivative ## sympy 라이브러리에 있는 sysbols와 Derivative를 이용하여, 문자에 대해 미분을 진행할 수 있다.

def solution(f,x0,e,N):
    x=symbols('x') # 미분하기 위해 x를 기호로 보기로 선언
    x_=x0 # 계속 갱신될 x절편의 값을 x_라고 하고, 초기값은 x0로 설정
    h=Derivative(f,x).doit() # f함수를 x에 대해 미분한 함수
    for _ in range(N): # N번 반복한다.
        x_=-float(f.doit().subs({x:x_}))/float(h.doit().subs({x:x_}))+float(x_) # subs함수를 이용해 문자 x 자리에 x_(실제 x값, 즉 이전에 구한 x 절편, 즉 x_)을 대입하여 x절편(x_)를 구한다.
        y_=float(f.doit().subs({x:x_})) # 구한 x절편에 해당하는 함수값(y값)을 구한다.
        if abs(y_)<e: # 함수값이 임계값보다 작다면
            break  # 반복문 탈출
    return x_ # 근, 즉 최종 x절편 값 반환

x=symbols('x') # x를 문자로 보기위해 sysbol 함수 사용
f=(x**2)**2-5*x*x**2+9*x+3 # 초기 식 선언
print(solution(f,6,0.0001,10)) #왼쪽부터 순서대로 사용할 함수, 초기값, 임계값, 반복수 이다.

