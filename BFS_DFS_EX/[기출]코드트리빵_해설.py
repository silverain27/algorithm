import sys
from collections import deque

# -----------------입력 끝 -----------------
# -----------------입력 끝 -----------------
INT_MAX = sys.maxsize
EMPTY = (-1, -1)

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

# 0이면 빈 칸, 1이면 베이스 캠프, 2라면 아무도 갈 수 없는 곳을 뜻합니다.
grid = [list(map(int, input().split())) for _ in range(n)]

# 각 사람이 가고 싶어 하는 편의점 위치 
store_list = []
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    store_list.append((x - 1, y - 1))

# 현재 사람들의 위치를 관리합니다.
# 처음엔 격자 밖에니까 Empty 로 둔다 
people = [EMPTY] * m

current_time = 0 #현재시간


dx = [-1,  0, 0, 1] #우선순위인 상좌우하 
dy = [ 0, -1, 1, 0]

# bfs에 사용되는 변수
step = [[0] * n for _ in range(n)] # 최단거리 결과 기록 일단 0으로 초기화 
visited = [[False] * n for _ in range(n)] 

# -----------------입력 끝 -----------------
# -----------------입력 끝 -----------------



def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
def can_go(x, y):
    # 범위를 벗어나지 않으면서, 방문했던 적이 없으면서, 이동 가능한 곳이어야 합니다.
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 2


# (a,b)를 시작으로 하는 BFS
# 시작점으로부터의 최단거리 결과는 step배열에 기록
def bfs(start_pos):
    # 1번만 돌리는거니까 visited, step 값을 전부 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0
    
    q = deque()
    q.append(start_pos)
    sx, sy = start_pos
    visited[sx][sy] = True
    step[sx][sy] = 0
 

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            if can_go(nx, ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))


# 시뮬레이션
def simulate():
    # Step 1. 격자에 있는 사람들에 한하여 편의점 방향을 향해 1칸 움직입니다.
    for i in range(m):
        # 아직 격자 밖에 있는 사람이거나 이미 편의점에 도착한 사람이라면 패스합니다.
        if people[i] == EMPTY or people[i] == store_list[i]:
            continue
        
        # 원래는 현재 위치에서 편의점 위치까지의 최단거리를 구해줘야 합니다.
        # 다만 최단거리가 되기 위한 그 다음 위치를 구하기 위해서는
        # 거꾸로 편의점 위치를 시작으로 현재 위치까지 오는 최단거리를 구해주는 것이 필요합니다.
        # 따라서 편의점 위치를 시작으로 하는 BFS를 진행합니다.
        bfs(store_list[i])

        px, py = people[i]
        # 현재 위치에서 상좌우하 중 최단거리 값이 가장 작은 곳을 고르면
        # 그 곳으로 이동하는 것이 최단거리 대로 이동하는 것이 됩니다.
        # 그러한 위치 중 상좌우하 우선순위대로 가장 적절한 곳을 골라줍니다.
        min_dist = INT_MAX
        min_x, min_y = -1, -1
        for k in range(4):
            nx, ny = px + dx[k], py + dy[k]
            if in_range(nx, ny) and visited[nx][ny] and min_dist > step[nx][ny]:
                min_dist = step[nx][ny]
                min_x, min_y = nx, ny

        # 우선순위가 가장 높은 위치로 한 칸 움직여줍니다.
        people[i] = (min_x, min_y)

    # Step 2. 편의점에 도착한 사람에 한하여 
    #         앞으로 이동 불가능하다는 표시로 
    #         grid값을 2로 바꿔줍니다.
    for i in range(m):
        if people[i] == store_list[i]:
            px, py = people[i]
            grid[px][py] = 2

    # Step 3. 현재 시간 current_time에 대해 current_time ≤ m를 만족한다면
    #         t번 사람이 베이스 캠프로 이동합니다.

    # current_time가 m보다 크다면 패스합니다.
    if current_time > m:
        return
    
    # Step 3-1. 편의점으로부터 가장 가까운 베이스 캠프를 고르기 위해
    #           편의점을 시작으로 하는 BFS를 진행합니다.
    bfs(store_list[current_time - 1])  

    # Step 3-2. 편의점에서 가장 가까운 베이스 캠프를 선택합니다.
    #           i, j가 증가하는 순으로 돌리기 때문에
    #           가장 가까운 베이스 캠프가 여러 가지여도
    #           알아서 (행, 열) 우선순위대로 골라집니다.
    min_dist = INT_MAX
    min_x, min_y = -1, -1
    for i in range(n):
        for j in range(n):
            # 베이스 캠프 중에 방문 한적 없는 애들 중, 제일 값이 작은애 
            # 거리가 가장 가까운 위치를 찾아줍니다.
            # step[i][j] 보다 작은게 있으면 계속 업데이트를 해준다 
            if visited[i][j] and grid[i][j] == 1 and min_dist > step[i][j]:
                min_dist = step[i][j]
                min_x, min_y = i, j
    # 우선순위가 가장 높은 베이스 캠프로 이동합니다.
    people[current_time - 1] = (min_x, min_y)
    # 해당 베이스 캠프는 앞으로 이동이 불가능한 칸임을 표시합니다.
    grid[min_x][min_y] = 2 #원래는 0 아니면 1이었기 때문에 2로 표시된 곳은 방문 불가 


# 전부 편의점에 도착헀는지를 확인합니다.
def end():
    # 단 한 사람이라도
    # 편의점에 도착하지 못했다면
    # 아직 끝나지 않은 것입니다.
    for i in range(m):
        if people[i] != store_list[i]:
            return False

    # 전부 편의점에 도착했다면 끝입니다.
    return True


# 1분에 한번씩 시뮬레이션을 진행합니다.
while True:
    current_time += 1
    simulate()
    # 전부 이동이 끝났다면 종료합니다.
    if end(): 
        break

print(current_time)