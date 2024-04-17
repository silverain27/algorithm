from collections import deque   
import sys
graph = []
N = int(input())

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
#print(graph)
#단지번호 문제랑 유사한데 여러개를 돌리는 느낌임 

height = 0
for i in range(N):
    height = max(height,max(graph[i])) #제일 큰 물높이 구한다음 
    
    
newgraph = [[-1]*N for _ in range(N)]
answer_count = 0 # 최대 영역 반환할 갯수 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y, gp):
    count = 0
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N: #범위안
                if gp[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    count +=1
    return count

answer_count = 0
for ht in range(height):
    result= []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] <=ht: #물에 잠기면 0
                newgraph[i][j] = 0
            else:
                newgraph[i][j] = 1 #물에 안잠기면 1 
    #그래프를 다 만들었을때
    visited = [[False]* N for _ in range(N)] #다시 초기화 
    #print("--새로운 그래프 : ", "물 높이 : ", ht, newgraph)
    for aa in range(N):
        for bb in range(N):
            if visited[aa][bb] == False and newgraph[aa][bb] == 1:
                cnt = bfs(aa,bb, newgraph) ## 만든 새로운 그래프를 bfs돌려줌  
                #print(cnt)
                result.append(cnt)
    answer_count = max(answer_count, len(result))
print(answer_count)

            
    