EMPTY = (-1, -1, -1, -1, -1, -1)

# 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))

# 총 목록 GUN !!!! 
gun = [[[] for _ in range(n)]for _ in range(n)]
for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        if nums[j] != 0:
            gun[i][j].append(nums[j]) #1칸에 총이 여러개 들어있을수도 있기 때문에 ! 

# 각 칸마다 플레이어 정보를 관리합니다.
# 순서대로 (num, x, y, d, s, a) 정보를 관리합니다.
# (x, y)위치에서 방향 d를 보고 있으며
# 초기 능력치가 s인 num번 플레이어가
# 공격력이 a인 총을 들고 있음을 뜻합니다.
# 총이 없으면 a는 0입니다.
players = []
for i in range(m):
    x, y, d, s = tuple(map(int, input().split()))
    players.append((i, x - 1, y - 1, d, s, 0)) #처음에는 아무것도 안가지고 있다를 표시 ! 0으로 

# 방향 순서대로 
# dx, dy를 정의합니다.
# ↑, →, ↓, ←
dxs = [-1, 0, 1,  0]
dys = [ 0, 1, 0, -1]

# 플레이어들의 포인트 정보를 기록합니다.
points = [0] * m


# (x, y)가 격자를 벗어나는지 확인합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 현재 (x, y)위치에서 방향 d를 보고 있을 때 다음 위치와 방향을 찾아줍니다.
def get_next(x, y, d):
    nx, ny = x + dxs[d], y + dys[d]
    # 격자를 벗어나면
    # 방향을 뒤집어
    # 반대 방향으로 한 칸 이동합니다.
    if not in_range(nx, ny):
        # 반대 방향 : 0 <. 2 / 1 <. 3
        d = (d + 2) if d < 2 else (d - 2)
        nx, ny = x + dxs[d], y + dys[d]

    return (nx, ny, d)


# 해당 칸에 있는 Player를 찾아줍니다.
# 없다면 EMPTY를 반환합니다.
def find_player(pos):
    for i in range(m):
        _, x, y, _, _, _ = players[i]
        if pos == (x, y):
            return players[i]

    return EMPTY


# Player p의 정보를 갱신해줍니다.
def update(p):
    players[p[0]] =p 
  
# 플레이어 p를 pos 위치로 이동시켜줍니다.
def move(p, pos):
    num, x, y, d, s, a = p
    nx, ny = pos

    # 가장 좋은 총으로 갱신해줍니다.
    gun[nx][ny].append(a) #총을 일단 넣고 
    gun[nx][ny].sort(reverse=True) #총을 소팅한다음에 
    a = gun[nx][ny][0] #제일 앞에 있는 총이 젤 좋은거니까 
    gun[nx][ny].pop(0) #얘를 들고나간다.

    p = (num, nx, ny, d, s, a) #p가 위치도 바뀌고 총 공격력도 바꼈으니까 업데이트시켜줌 
    update(p)


# 진 사람의 움직임을 진행합니다.
# 결투에서 패배한 위치는 pos입니다.
def loser_move(p):
    num, x, y, d, s, a = p
    
    # 먼저 현재 위치에 총을 내려놓게 됩니다.
    gun[x][y].append(a)

    # 빈 공간을 찾아 이동하게 됩니다.
    # 현재 방향에서 시작하여
    # 90'씩 시계방향으로
    # 회전하다가 
    # 비어있는 최초의 곳으로 이동합니다.
    for i in range(4):
        ndir = (d + i) % 4 
        # 일단 현재방향부터 어느 방향부터 갈지 정하는 거 
        # 현재 방향이 2 이면 
        # 2 + 0 % 4 니까 2부터 시작한다 
        nx, ny = x + dxs[ndir], y + dys[ndir]

        #일단 현재 방향 부터 했는데 격자 밖이거나 / 플레이어가 있으면 90도 돌려줌 
        if in_range(nx, ny) and find_player((nx, ny)) == EMPTY:
            p = (num, x, y, ndir, s, 0) # 일단 총을 내려놓고 벙향대로 움직여야한다 
            move(p, (nx, ny))
            break


# p2과 p2가 pos에서 만나 결투를 진행합니다.
def duel(p1, p2, pos):
    num1, _, _, d1, s1, a1 = p1
    num2, _, _, d2, s2, a2 = p2

    # (초기 능력치 + 총의 공격력, 초기 능력치) 순으로 우선순위를 매겨 비교합니다.

    # p1이 이긴 경우
    if (s1 + a1, s1) > (s2 + a2, s2):
        # p1은 포인트를 얻게 됩니다.
        points[num1] += (s1 + a1) - (s2 + a2)
        # p2는 진 사람의 움직임을 진행합니다.
        loser_move(p2)
        # 이후 p1은 이긴 사람의 움직임을 진행합니다.
        move(p1, pos)
    # p2가 이긴 경우
    else:
        # p2는 포인트를 얻게 됩니다.
        points[num2] += (s2 + a2) - (s1 + a1)
        # p1은 진 사람의 움직임을 진행합니다.
        loser_move(p1)
        # 이후 p2는 이긴 사람의 움직임을 진행합니다.
        move(p2, pos)


# 1라운드를 진행합니다.
def simulate():
    # 첫 번째 플레이어부터 순서대로 진행합니다.
    for i in range(m):
        num, x, y, d, s, a = players[i]

        # Step 1-1. 현재 플레이어가 움직일 그 다음 위치와 방향을 구합니다.
        nx, ny, ndir = get_next(x, y, d)
        
        # 해당 위치에 있는 전 플레이어 정보를 얻어옵니다.
        next_player = find_player((nx, ny))
        
        # 현재 플레이어의 위치와 방향을 보정해줍니다.
        curr_player = (num, nx, ny, ndir, s, a)
        update(curr_player)
        
        # Step 2. 해당 위치로 이동해봅니다.
        # Step 2-1. 해당 위치에 플레이어가 없다면 그대로 움직입니다.
        if next_player == EMPTY:
            move(curr_player, (nx, ny))
        # Step 2-2. 해당 위치에 플레이어가 있다면 결투를 진행합니다.
        else:
            duel(curr_player, next_player, (nx, ny))

# k번에 걸쳐 시뮬레이션을 진행합니다.
for _ in range(k):
    simulate()

# 각 플레이어가 획득한 포인트를 출력합니다.
for point in points:
    print(point, end=" ")