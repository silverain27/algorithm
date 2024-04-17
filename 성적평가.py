import sys

N = int(input())

SCORE = [] # 각 회차별 점수 저장 
for _ in range(3):
    SCORE.append(list(map(int, sys.stdin.readline().split())))

SUM = [0 for _ in range(N)] # 점수 합계
RANK = [] # 회차별 등수
SUM_RANK = [] # 점수 합산 등수

# 병합 정렬 구현
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] > high_arr[h]: # 내림차순이므로 부등호 방향 변경
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    print("la", low_arr, l)
    print("ha", high_arr, h)
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

# 회차 별 등수 출력
for score in SCORE:
    dic = {}
    idx = 0
    sorted_score = merge_sort(score)
    for s in sorted_score:
        idx += 1
        if s not in dic:
            dic[s] = idx

    arr = []
    for i in range(len(score)):
        arr.append(dic[score[i]])
        SUM[i] += score[i]
    print(*arr)

# 합산 점수 등수 출력
dic = {}
idx = 0
sorted_sum = merge_sort(SUM)
for s in sorted_sum:
    idx += 1
    if s not in dic:
        dic[s] = idx

arr = []
for i in range(len(sorted_sum)):
    arr.append(dic[SUM[i]])
print(*arr)


