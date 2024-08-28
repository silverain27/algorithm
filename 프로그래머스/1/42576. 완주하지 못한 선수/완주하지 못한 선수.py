'''
import collections
def solution(participants, completions):
    a = collections.Counter(participants)
    b = collections.Counter(completions)
    
    return list((a-b).keys())[0]

def solution(participants, completions):
    total_par = {}
    total_com = {}
    for par in participants:
        if par not in total_par:
            total_par[par] = 1
        else:
            total_par[par] +=1
    for com in completions:
        if com not in total_com:
            total_com[com] = 1
        else:
            total_com[com] +=1
    
    for par in total_par:
        if par in total_com:
            total_par[par] -= total_com[par]
    
    for par in total_par:
        if total_par[par] == 1:
            return par
'''   
def solution(participants, completions):
    maraton = {}
    for part in participants:
        if part not in maraton:
            maraton[part] = 1
        else:
            maraton[part] +=1
    for compl in completions:
        if compl in maraton:
            maraton[compl] -=1
    for key,value in maraton.items():
        if value != 0:
            return key
    
    
    