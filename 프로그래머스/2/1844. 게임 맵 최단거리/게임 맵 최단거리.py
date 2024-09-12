from collections import deque

def solution(maps):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r = len(maps) #세로크기
    c = len(maps[0]) #가로크기 

    visited = [[-1 for _ in range(c)] for _ in range(r)]
    
    print(visited)
    

    queue = deque()
    queue.append([0, 0])

    visited[0][0] = 1

    while queue:
        y, x = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])

    answer = visited[-1][-1]
    return answer


