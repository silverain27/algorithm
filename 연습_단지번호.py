# 혼자 단지번호 

from collections import deque

N = int(input())
graph = []
#visited = []
result= []

visited_real = []
for i in range(N):
    graph.append(list(map(int, input())))
    #visited.append([False]*N) ##visited만들어주는 부분 정확히 하기 
    
#visited = [[False] * N] * N 
visited = [[False]*N for _ in range(N)]
print("---visited", visited)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    count = 0
    while queue:
        a, b = queue.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if nx<0 or nx>=N or ny <0 or ny>=N: ##패스 해주는 부분을 or로 조건 명확히 ! 
                continue
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                
                count +=1
    return count 
                
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            count = bfs(i,j)
            result.append(count)
    
print(len(result))
result.sort()
for res in result:
    print(res+1)