#np.array는 행렬의 상수배 연산 가능 / 파이썬 리스트는 불가능
import numpy as np

def gaussian_elimination(matrix):
    
    #행렬의 가로 세로 
    W = len(matrix[0])
    H = len(matrix)
    

    print("최초상태")
    print(matrix, "\n")
    
    # uppertriangular
    print("uppertriangular matrix 형태로 변환")
    row = 0 #첫행 선택
    for col in range(W-2): #b=W-1, 0 ~ W-3 까지 반복(열)

        #상수배 후 덧셈연산
        for j in range(row+1,H): # 첫행 다음 행 ~ 끝까지(첫행은 그대로 둠)
            if matrix[j][col] != 0: # [j]번째행의 [col]번째 열
                
                matrix[j] = matrix[j] - (matrix[j][col]/matrix[row][col]) * matrix[row]

            
        row += 1 #첫행 바꿔줌
        print(matrix, "\n")

        # 열이 정해지고 행이 바껴
        # (시작지점 : a11)열 1개 당 행이 다 바뀜. -> 첫행(기준행)바꿔줌
        # -> 2번째 열로 넘어감(시작지점이 a22) 

    # lowertriangular
    print("lowertriangular matrix 형태로 변환")
    row = H-1 #여기서는 첫행 : H-1, 끝행 : 0
    for col in range(W-2,0,-1): #b=W-1, W-2 ~ 1까지 반복(열)

        #상수배 후 덧셈연산
        for j in range(row-1,-1, -1): # 첫행:row. 첫행 다음 행:row-1. 마지막 행:0 (마지막 0번째행까지 실행돼야함 )
            if matrix[j][col] != 0: # [j]번째행의 [col]번째 열
                
                matrix[j] = matrix[j] - (matrix[j][col]/matrix[row][col]) * matrix[row]

        row -= 1 #row = row - 1, 첫행 바꿔줌.
        print(matrix, "\n")
 
    print("방정식의 해는")
    answer=[]
    for i in range(H): #0행 ~ H-1행까지 반복
        answer.append(matrix[i][W-1]/matrix[i][i])
    print(answer)
    return 

#임의의 행렬 생성
my_matrix=[]
n=int(input("어떤 N x N 행렬을 만드시겠습니까? (숫자입력)"))
for i in range(n):
    my_matrix.append(list(map(float,input(f"{i+1}번째 행을 입력해주세요. 요소 간 구분은 스페이스 바(공백)으로 해주세요.").split())))

matrix = np.array(my_matrix)
gaussian_elimination(matrix)
