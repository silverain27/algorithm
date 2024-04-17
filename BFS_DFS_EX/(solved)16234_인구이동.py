#인구이동 

from collections import deque
N, L, R = map(int, input().split())

popul  = []
for i in range(N):
    popul.append(list(map(int, input().split())))
    

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def BFS(x,y):
    
    union = [] # 얘를 BFS돌때마다 만드는거기때문에 여기 안에다 넣는게 중요 ! ! POINT ! ! 
    queue = deque()
    queue.append((x,y))
    union.append((x,y))
    
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0: #일단 범위 안에 있고 방문안했으면 
                if L<=abs(popul[a][b] - popul[nx][ny])<=R: # 이 사이값이면 
                    ######여기서 틀림 ######
                    #여기서 꺼낸애랑 아닌애 차이를 비교해야한다 
                    union.append((nx,ny)) #좌표값 일단 넣어준다. 
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
    return union

result = 0
while 1:         
    visited = [[0]*(N) for _ in range(N)] 
    flag =0 
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = BFS(i,j)
                if(len(country)>1):
                    #days +=1 
                    #날짜를 여기서 세주면 안되는 이유는 
                    #전체를 다 검색해서 나오는 여러 union에 대해서 
                    # 한번 수행하는거니까 전체를 다 돌고난 다음에 day +1 를 해줘야함 
                    flag =1 
                    #number = sum([popul[x][y] for x,y in country]) // len(country)
                    summ = 0
                    for xx,yy in country:
                        summ += popul[xx][yy]
                    #print(number)
                    for xx, yy in country:
                        #print(xx,yy)
                        popul[xx][yy]= int(summ // len(country))
                    
                    print(int(summ // len(country)))
                    print(popul)
    
    if flag == 0:
        break
    result += 1 # 전체 다 돌고나서 +1해준다 
print(result)     
#print(popul)

        
                        