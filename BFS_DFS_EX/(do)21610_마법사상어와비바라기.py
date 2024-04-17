N,M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

command = [tuple(map(int, input().split())) for _ in range(M)]

#=N,M = 5,8
#paper = [[0,0,1,0,2], [2,3,2,1,0], [0,0,2,0,0], [1,0,2,0,0], [0,0,2,1,0]]
#paper = [[100,100,100,100,100],[100,100,100,100,100],[100,100,100,100,100],[100,100,100,100,100],[100,100,100,100,100]]
#command = [[8,1],[7,1],[6,1],[5,1],[4,1],[3,1],[2,1],[1,1]]


dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

cloud = [[N-1,0], [N-1,1], [N-2,0],[N-2,1]] # 비구름 위치 

# step 1
for i in range(len(command)):
    visited = [[False for _ in range(N)] for _ in range(N)]
    for j in range(len(cloud)):
        cloud[j][0] += dx[command[i][0]-1] * command[i][1]
        cloud[j][1] += dy[command[i][0]-1] * command[i][1]
        
        cloud[j][0] %= N
        cloud[j][1] %= N
        visited[cloud[j][0]][cloud[j][1]] = True
   
    # step 2 비의 양 +1
    for (x,y) in cloud:
        paper[x][y] +=1
    

    # step 4 물복사 버그 마법
    
    for (x,y) in cloud: 
        count =0
        for k in range(len(dx)):
            if k%2 ==1:
                cx = x+dx[k]
                cy = y+dy[k]
                if(0<=cx<N and 0<=cy<N and paper[cx][cy]>0): #물이 있으면
                    count+=1
                     
        paper[x][y] +=count
    
    
    next_clouds = []
    for i in range(N):
        for j in range(N):
            '''
            if [i,j] not in cloud and paper[i][j] >=2:
                next_clouds.append([i,j])
                paper[i][j]-=2
            '''
            if visited[i][j] == False and paper[i][j] >=2:
                next_clouds.append([i,j])
                paper[i][j]-=2
    # stel 3 구름이 모드 사라짐 
    cloud = []
    cloud = next_clouds
    
    answer = 0
    for i in range(N):
        for j in range(N):
            answer += paper[i][j]

print(answer)


        
        