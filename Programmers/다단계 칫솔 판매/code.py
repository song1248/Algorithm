from collections import defaultdict
def solution(enroll, referral, seller, amount):
    
    # 자식 : 부모 형태로 dictionary를 만듬
    enroll_dict = defaultdict(str)
    # 정답을 dictionary에 담음 (시간복잡도를 줄이기 위함)
    answer_dict = defaultdict(int)
    
    # 자식 : 부모 dictionary
    for en_idx, se in enumerate(referral):
        enroll_dict[enroll[en_idx]] = se 
    
    # 자식 -> 부모 로 탐색해가며 money를 추가
    for sllr, amnt in zip(seller, amount):
        money = amnt * 100
        s_money = 0
        p_money = 0
        
        # 현재 seller에 90% 추가하고( money - int(monoey(1/10)))
        # 부모노드로 이동
        # center에 도착하면 종료
        while sllr != '-':
            p_money = int(money * (10/100))
            s_money = money - p_money
            if p_money < 1:
                answer_dict[sllr] += money
                break
            else:
                answer_dict[sllr] += s_money
                sllr = enroll_dict[sllr]
                money = p_money
                
    answer = []
    for en in enroll:
        answer.append(answer_dict[en])

    return answer
