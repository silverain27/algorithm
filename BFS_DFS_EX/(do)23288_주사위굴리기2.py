from collections import deque
import sys

def BFS(x, y, color):
    score =0
    visited = [[0] * M for _ in range(N)]  # 방문체크
    q = deque()
    q.append([x, y])
    dx = [0,1,0,-1] #동 남 서 북
    dy = [1,0,-1,0]

    blocks = [(x,y)]  # 블록좌표 넣을 리스트, 무지개좌표 넣을 리스트

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            #print(nx,ny)
            # 범위 안이면서 방문 안한 일반 블록인 경우
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and paper[nx][ny] == color:
                visited[nx][ny] = 1
                q.append([nx, ny])
                blocks.append((nx, ny))
        blocks = list(set(blocks))
        score = color * len(blocks)
                
    return [score, blocks]


#방향 계산 

#동서남북으로 연속해서 이동할 수 있는 칸 : bfs로 구함




def changeDice(direction):
    
    global dice
    up, down, left, right, front, back = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] #위 아래 왼 오른 앞 뒤
    if(direction == 0 ): #동 
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]  = left, right, down, up, front, back
    elif(direction ==1): #남 
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]  = back,front, left, right, up, down
    elif(direction == 2): #서
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]  = right, left, up, down, front, back
    elif(direction ==3): #북
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]  = front,back, left, right, down,up
        

def rotDirection(clock):
    global direction
    if(clock == True): # 시계방향이면 
        direction +=1
        if(direction ==4):
            direction =0
    else: #반시계방향이면 
        if(direction ==0):
            direction =3
        else:
            direction -=1
        


x,y =0,0
direction = 0 #처음은 동쪽 
score = 0
answer_score =0
N,M,K = map(int, input().split())
dx = [0,1,0,-1] #동 남 서 북
dy = [1,0,-1,0]

dice = [1,6,4,3,5,2] #주사위 위 아래 왼 오른 앞 뒤 
paper = [list(map(int, input().split())) for _ in range(N)]

for i in range(K):
    #print("direction : ", direction)
    ## 1번 ## 주사위가 이동방향으로 한칸 굴러간다. 
    cx,cy = x+dx[direction], y+dy[direction]
    if(0<=cx<N and 0<=cy<M):
        changeDice(direction)
    else:
        cx -= dx[direction]
        cy -= dy[direction]
        if direction ==0 or direction ==2:
            direction = abs(direction-2)
        elif direction ==3:
            direction =1
        elif direction ==1:
            direction =3
        
        
        
        cx += dx[direction]
        cy += dy[direction]
        
        
        changeDice(direction)
        
    ## 2번 ## BFS 점수 획득 
    score, answer_block = BFS(cx,cy, paper[cx][cy])
    answer_score += score
    # 3번 ##  이동방향 바꿔주기 
    if(dice[1] > paper[cx][cy]): #A>B인경우     
        rotDirection(True) #시계방향으로 
    elif dice[1] < paper[cx][cy]:
        rotDirection(False) #반시계방향으로 

    x,y = cx,cy 

print(answer_score)
    