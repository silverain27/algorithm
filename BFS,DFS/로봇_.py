# n,m = map(int,input().split(' '))

# x,y,d = map(int,input().split(' '))

def solution():

    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    n,m = (11,10)
    p_y,p_x,p_d = (7,4,0)
    robot_map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    count = 0
    while True:

        print("p_y,x,d :", p_y,p_x,p_d)
        print("robot_map")
        for k in range(n):
            print(robot_map[k])
        print("count", count)

        if robot_map[p_y][p_x] == 0:
            count += 1
            robot_map[p_y][p_x] = 2

        isCleaned = True

 

        for i in range(4):
            n_d = (p_d+i)%4
            n_y = p_y + dy[n_d]
            n_x = p_x + dx[n_d]
            if robot_map[n_y][n_x] == 0:
                isCleaned = False
        print(isCleaned)
        if isCleaned == False:
            p_d = (p_d-1)%4
            n_y = p_y + dy[p_d]
            n_x = p_x + dx[p_d]
            if robot_map[n_y][n_x] == 0:
                p_y,p_x,p_d = (n_y,n_x,p_d)
        else:
            p_y = p_y-dy[p_d]
            p_x = p_x-dx[p_d]
            if robot_map[p_y][p_x] == 1:
                print(count)
                return 0
solution()