import numpy as np
import math
def QR_Decomposition(A):
    n, m = A.shape # shape 함수를 통해, 행 과 열의 수를 구할 수 있음
    Q = np.empty((n, n)) # 빈 matrix 생성 (모든 요소 값 0)
    u = np.empty((n, n)) # 빈 matrix 생성 (모든 요소 값 0)

    u[:, 0] = A[:, 0] # A의 첫번째 열 (벡터)를 u의 첫번째 벡터로 정함 (A1=U1)
    Q[:, 0] = u[:, 0] /math.sqrt(np.dot(u[:, 0], u[:, 0])) # u벡터를 u벡터의 크기로 나눠줌으로써 정규화 함 (Q1=U1/|U1|)

    for i in range(1, n):

        u[:, i] = A[:, i] # 먼저 이렇게 설정 (Ui=Ai)
        for j in range(i):
             u[:,i]=u[:,i]-(np.dot(A[:, i], Q[:, j]) / np.dot(Q[:, j], Q[:, j])) * Q[:, j] # Ui = Ui-proj값 --> Ui= Ai-proj값

        Q[:, i] = u[:, i] / math.sqrt(np.dot(u[:, i], u[:, i])) # u벡터를 u벡터의 크기로 나눠줌으로써 정규화 함 (Qi=Ui/|Ui|)

    R = np.zeros((n, m)) # 빈 matrix 생성 (모든 요소 값 0)
    for i in range(n): # 각 행에 대해서
        for j in range(i, m):  # 각 열에 대해서
            R[i, j] = (np.dot(A[:, j], Q[:, i]) / np.dot(Q[:, i], Q[:, i]) ) # Aj를 Qi로 proj 한 값의 크기

    return Q, R # Q와 R을 리턴

matirx=[[3,2],[1,2]]
matirx=np.array(matirx) # numpy array 형태로 변경 (numpy 함수를 사용하기 위해 형태 변경)
Q,R=QR_Decomposition(matirx)
print(Q) # Q 출력
print()
print(R) # R 출력
