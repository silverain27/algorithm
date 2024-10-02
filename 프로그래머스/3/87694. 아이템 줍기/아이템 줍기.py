from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1]*102 for _ in range(102)]
    visited = [[0]*102 for _ in range(102)]
    
    # 길이가 1인 모든 선분 저장
    edges = set()
    for elem in rectangle:
        lx,ly,rx,ry = map(lambda x:x*2, elem)
        for i in range(lx, rx+1):
            for j in range(ly, ry+1):
                if lx<i<rx and ly<j<ry:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1
            
    # bfs 시작
    dxs = [0,0,1,-1]
    dys = [1,-1,0,0]
    q = deque()
    q.append((characterX*2,characterY*2))
    while q:
        x, y = q.popleft()
        if x == itemX*2 and y == itemY*2:
            answer = visited[x][y]//2
            break
        for dx, dy in zip(dxs, dys):
            nx, ny = dx+x, dy+y
            if 0<nx<102 and 0<ny<102 and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    return answer
