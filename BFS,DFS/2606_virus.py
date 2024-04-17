#2606 바이러스 

from collections import deque

N = int(input()) #컴퓨터 갯수
M = int(input()) #쌍 갯수

graph = [[] for i in range(N+1)] 
visited = [False]*(N+1)
cnt = 0
## !! 그래프 초기화 : 비어있는 걸로 , 총 컴퓨터 갯수보다 1개 많게 
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b) ##양방향/ 단방향 그래프인지 확인 
    graph[b].append(a)
    
def bfs( v):
    global cnt
    queue = deque() 
    queue.append(v)
    while queue: 
        pop = queue.popleft() 
        visited[pop] = True

        for i in graph[pop]:
            if visited[i]==False:
                visited[i] = True
                queue.append(i) 
                cnt += 1 
    print(cnt)
    
def dfs(v):
    visited[v] = True
    global cnt
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)

dfs(1)    
print(cnt) 

#bfs(1)
