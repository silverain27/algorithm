# 14502 연구소

from collections import deque
import sys
import copy

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#바이러스 퍼뜨리기 및 최대 영역 크기 갱신
def bfs():
    global max_result
    queue=deque()
    tmp=copy.deepcopy(graph)
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==2:
                queue.append((i,j))
    # 이문제는 여기서 큐를 생성하는게 다르다는 포인트 ! !
    # 토마토를 생각해 ! 
    
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and ny>=0 and ny<n and nx<m:
                if tmp[ny][nx]==0:
                    tmp[ny][nx]=2
                    queue.append((ny,nx))
    result=0   
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                result+=1
    max_result=max(result,max_result)

#벽 세우기
def build(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                build(cnt+1)
                graph[i][j]=0 
                #이게 포인트인듯.. 벽을 세울 수 있는 모든 경우를 체크 해줘야하기 때문에
                #재귀 뒤에 graph[i][j]=0을 꼭 넣어줘야함 
                
n,m=map(int,sys.stdin.readline().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
max_result=0
    
build(0)
print(max_result)