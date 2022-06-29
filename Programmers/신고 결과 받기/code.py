from collections import defaultdict
def solution(id_list, report, k):
    
    answer = [0 for i in id_list]
    report = list(set(report))
    report = [x.split() for x in report]
    
    # 신고 받은 수 세기
    reported_count = defaultdict(int)
    for reporter, ported in report:
        reported_count[ported] += 1
    
    # 연산량 줄일려고 dictionary로 만들기
    dict = {}
    for i,name in enumerate(id_list):
        dict[name] = i
    
    
    for name in id_list:        
        if reported_count[name] >= k:
            for reporting, reported in report:
                if reported == name:
                    answer[dict[reporting]] +=1

    return answer
