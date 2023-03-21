#사다리꼴 공식
import math # 루트를 사용하기 위해 라이브러리 불러옴
def f(x): #함수 값을 출력하기 위한 함수
    return math.sqrt(x) #함수 값 출력

def trapezoidal(interval,partition_num): #입력의로 구간과 분할 수를 받음
    start,end=interval #시작점과 끝점을 받음
    result=0
    dx=(end-start)/partition_num 
    for i in range(partition_num): 
        result+=(dx)*(f(start+(i+1)*dx)+f(start+i*dx))/2 #사다리꼴 넓이 공식 사용
    return result

print(trapezoidal([0,2],10))
