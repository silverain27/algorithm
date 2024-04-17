# 맥주마시면서 걸어가기
import sys
from collections import deque
input = sys.stdin.readline

    
def bfs():
    q = deque()
    q.append([home[0], home[1]]) #일단 집을 넣는다  
    while q:
        x, y = q.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000:
            print("happy")
            return
        for i in range(n): #편의점 갯수 만큼 넣어줌 
            if not visited[i]:
                new_x, new_y = conv[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    q.append([new_x, new_y])
                    visited[i] = 1
    print("sad")
    return


TEST = int(input()) #테스트 케이스 수 
for i in range(TEST):
    n = int(input()) # 편의점이 몇개냐 ?
    home = list(map(int,input().split())) # 상근이 집 출발 위치 
    conv = []
    for j in range(n):
        x, y = map(int, input().split())
        conv.append([x, y]) # 편의점 위치 
    fest = list(map(int,input().split())) # 페스티벌 위치 
    visited = [0 for i in range(n+1)] #home 제외 편의점갯수 만큼 
    bfs()