MAX_N = 100000
MAX_M = 100000

# 변수 선언
n, m, q = -1, -1, -1

# id에 해당하는 상자의 nxt값과 prv값을 관리합니다.
# 0이면 없다는 뜻입니다.
prv, nxt = [0] * (MAX_M + 1), [0] * (MAX_M + 1)

# 각 벨트별로 head, tail id, 그리고 총 선물 수를 관리합니다.
# 0이면 없다는 뜻입니다.
head, tail, num_gift = [0] * MAX_N, [0] * MAX_N, [0] * MAX_N


# 공장 설립
def build_factory(elems):
    # 공장 정보를 입력받습니다.
    n, m = elems[1], elems[2] #4,6 4는 벨트갯수, 6은 상자갯수 
    
    # 벨트 정보를 만들어줍니다.
    boxes = [[] for _ in range(n)]
    for _id in range(1, m + 1):
        b_num = elems[_id + 2]
        b_num -= 1
        
        boxes[b_num].append(_id)

    # 초기 벨트의 head, tail, nxt, prv값을 설정해줍니다.
    for i in range(n):
        # 비어있는 벨트라면 패스합니다.
        if len(boxes[i]) == 0:
            continue
        
        # head, tail을 설정해줍니다.
        head[i] = boxes[i][0]
        tail[i] = boxes[i][-1]

        # 벨트 내 선물 총 수를 관리해줍니다.
        num_gift[i] = len(boxes[i])

        # nxt, prv를 설정해줍니다.
        for j in range(len(boxes[i]) - 1):
            nxt[boxes[i][j]] = boxes[i][j + 1]
            prv[boxes[i][j + 1]] = boxes[i][j]


# 물건을 전부 옮겨줍니다.
def move(elems):
    starts, finals = elems[1] - 1, elems[2] - 1 #이거는 벨트 번호다 

    # starts에 물건이 없다면 그대로 finals내 물건 수가 답
    if num_gift[starts] == 0:
        print(num_gift[finals])
        return

    # finals에 물건이 없다면 해당 벨트의 tail이랑 head만 바꾸면 됨 
    if num_gift[finals] == 0:
        head[finals] = head[starts]
        tail[finals] = tail[starts]
    else:
        orig_head = head[finals]
        # finals의 head를 교체해줍니다.
        head[finals] = head[starts]
        # starts의 tail과 기존 finals의 head를 연결해줍니다.
        src_tail = tail[starts]
        nxt[src_tail] = orig_head
        prv[orig_head] = src_tail

    # 벨트에 있는 모든 물건을 옮기는거니까 처음에 있던 벨트의 head, tail은 0이됨 
    head[starts] = tail[starts] = 0

    # 선물 상자 수를 갱신해줍니다.
    num_gift[finals] += num_gift[starts]
    num_gift[starts] = 0

    print(num_gift[finals])

# 해당 벨트의 head를 제거합니다.
def remove_head(b_num):
    # 불가능하면 패스합니다.
    if not num_gift[b_num]:
        return 0
    
    # 노드가 1개라면
    # head, tail 전부 삭제 후
    # 반환합니다.
    #1개였으면 원래 얘랑 연결되어있는 prev랑 next가 없었을거니까 고려를 안해줘도됨 
    # ---- 변경해야하는 거 해당 벨트의 head, tail -----
    if num_gift[b_num] == 1:
        _id = head[b_num]
        head[b_num] = tail[b_num] = 0 
        num_gift[b_num] = 0
        return _id

    # 값이 있었으면
    # 원래 next, prev, head, num gift 를 다바꿔주기 
    hid = head[b_num] #1
    next_head = nxt[hid] #5
    nxt[hid] = prv[next_head] = 0 #1의 next, 1의 prev를 없앤다 
    num_gift[b_num] -= 1 # 1번벨트의 선물갯수 줄이고 
    head[b_num] = next_head #head를 변경해준다

    return hid # 삭제하려는 박스 번호 



# 300 2 4 앞 물건을 교체해줍니다.
def change(elems):
    starts, finals = elems[1] - 1, elems[2] - 1
    #2번벨트 4번벨트의 젤 앞 물건을 바꿔준다 

    src_head = remove_head(starts)
    dst_head = remove_head(finals)
    push_head(finals, src_head) 
    push_head(starts, dst_head)
    
    print(num_gift[finals])




#  400 4 2 물건을 나눠옮겨줍니다.
def divide(elems):
    starts, finals = elems[1] - 1, elems[2] - 1

    # 순서대로 src에서 박스들을 빼줍니다.
    cnt = num_gift[starts]
    box_ids = []
    for _ in range(cnt // 2): #몫이니까 1인경우는 자동으로 안한다 
        box_ids.append(remove_head(starts)) 
        #넣어줘야하는 박스 번호를 구해준다 head를 없애준다. 

    
    # 거꾸로 뒤집어서 하나씩 dst에 박스들을 넣어줍니다.
    for i in range(len(box_ids) - 1, -1, -1):
        push_head(finals, box_ids[i])

    print(num_gift[finals])


# 해당 밸트에 head를 추가합니다.
def push_head(b_num, hid):
    # 불가능한 경우는 진행하지 않습니다.
    if hid == 0:
        return

    # 비어있었다면
    # head, tail이 동시에 추가됩니다.
    if not num_gift[b_num]:
        head[b_num] = tail[b_num] = hid
        num_gift[b_num] = 1
    # 그렇지 않다면
    # head만 교체됩니다.
    else:
        orig_head = head[b_num] #1 5 가 있는데 2를 넣었다고 가정하면 
        nxt[hid] = orig_head #2의 next를 1로 
        prv[orig_head] = hid #1의 prev를 2로 
        head[b_num] = hid #head바꿔줌 
        num_gift[b_num] += 1





# 선물 점수를 얻습니다.
def gift_score(elems):
    p_num = elems[1]

    a = prv[p_num] if prv[p_num] != 0 else -1
    b = nxt[p_num] if nxt[p_num] != 0 else -1

    print(a + 2 * b)
 

# 벨트 정보를 얻습니다.
def belt_score(elems):
    b_num = elems[1] - 1

    a = head[b_num] if head[b_num] != 0 else -1
    b = tail[b_num] if tail[b_num] != 0 else -1
    c = num_gift[b_num]

    print(a + 2 * b + 3 * c)


# 입력:
q = int(input())
for _ in range(q):
    elems = list(map(int, input().split()))
    q_type = elems[0]

    if q_type == 100:
        build_factory(elems)
    elif q_type == 200:
        move(elems)
    elif q_type == 300:
        change(elems)
    elif q_type == 400:
        divide(elems)
    elif q_type == 500:
        gift_score(elems)
    else:
        belt_score(elems)