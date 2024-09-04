# def solution(p):
#     ans = [0] * len(p)
#     stack = [0]
#     for i in range(1, len(p)):
#         if p[i] < p[stack[-1]]:
#             for j in stack[::-1]:
#                 if p[i] < p[j]:
#                     ans[j] = i-j
#                     stack.remove(j)
#                 else:
#                     break
#         stack.append(i)
#     for i in range(0, len(stack)-1):
#         ans[stack[i]] = len(p) - stack[i] - 1
#     return ans
# https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python
# from collections import deque
# def solution(prices):
#     prices = deque(prices) #큐로만들고 
#     answer = [] #저장할 answer stack 만들고 
#     while prices:
#         price = prices.popleft()
#         sec = 0
#         for q in prices:
#             sec+=1
#             if price > q:
#                 break
#         answer.append(sec)
#     return answer
        
        
def solution(prices):
    length = len(prices)
    answer = [ i for i in range (length - 1, -1, -1)]
    
    stack = [0]
    for i in range (1, length, 1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer    
        