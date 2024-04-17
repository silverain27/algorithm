# 경쟁적 전염 18405

from collections import deque

N, K = map(int, input().split())  #N*N시험과에서 K는 바이러스 종류가 총 K번까지

virusmap = []

for i in range(N):
    virusmap.append(list(map(int, input().split())))

S, X, Y = map(int, input().split()) #s초가 지났을때 (x,y)에 있는 값 ? 



location = []
for i in range(len(virusmap)):
    for j in range(len(virusmap)):
        if virusmap[i][j] != 0:
            location.append((virusmap[i][j],i,j))

location = sorted(location, key = lambda x: x[0]) #일단 바이러스 번호순대로 
q = deque()

for k, lx, ly in location:
    q.append((k,lx,ly, 0))
    
def BFS(S):
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]    
    while q:
        kk, xx,yy, times = q.popleft()
        if times == S:
            break 
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0<=nx<N and 0<=ny<N and virusmap[nx][ny] == 0:
                q.append((kk, nx,ny, times+1))
                virusmap[nx][ny] = kk
BFS(S)
if virusmap[X-1][Y-1] ==0:
    print(0)
else:
    print(virusmap[X-1][Y-1])


