from collections import deque

# 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 보드 상태를 입력받는 함수
def move(x, y, dx, dy, board):
    count = 0
    # 벽을 만날 때까지 이동
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs(board, rx, ry, bx, by):
    n, m = len(board), len(board[0])
    queue = deque([(rx, ry, bx, by, 0)])  # 빨간 구슬, 파란 구슬 위치, 이동 횟수
    visited = set([(rx, ry, bx, by)])  # 방문한 위치 기록

    while queue:
        rx, ry, bx, by, depth = queue.popleft()

        # 10번 이상 움직이면 실패
        if depth >= 10:
            return -1

        # 4가지 방향으로 이동 시도
        for i in range(4):
            nrx, nry, r_count = move(rx, ry, dx[i], dy[i], board)
            nbx, nby, b_count = move(bx, by, dx[i], dy[i], board)

            # 파란 구슬이 구멍에 빠지면 실패
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬만 구멍에 빠지면 성공
            if board[nrx][nry] == 'O':
                return depth + 1

            # 둘 다 같은 위치에 있을 수 없으므로, 더 많이 이동한 구슬을 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if r_count > b_count:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            # 새로운 상태가 방문한 적이 없으면 큐에 추가
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, depth + 1))

    return -1

# 입력 처리
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# 빨간 구슬(R)과 파란 구슬(B)의 초기 위치 찾기
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

# BFS 실행
result = bfs(board, rx, ry, bx, by)
print(result)