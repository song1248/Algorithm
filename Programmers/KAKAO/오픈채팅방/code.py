# "[닉네임]님이 들어왔습니다."
# "[닉네임]님이 나갔습니다."
# 채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.
#  - 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
#  - 채팅방에서 닉네임을 변경한다.
# 닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.
# 채팅방은 중복 닉네임을 허용
# 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return
from collections import defaultdict

def solution(records):
    
    new_records = []
    id_name = defaultdict(str)
    for i, record in enumerate(records):
        ipt = record.split(' ')
        move, c_id, name = 0, 0, 0
        if len(ipt) == 2:
            move, c_id, name = ipt[0], ipt[1], id_name[ipt[1]]
        else:
            move, c_id, name = ipt 
        new_records.append([move, c_id, name])
        id_name[c_id] = name
     
    answer = []
    for move, c_id, name in new_records:
        if move == 'Enter':
            answer.append("" + id_name[c_id] + "님이 들어왔습니다.")
        elif move == 'Leave':
            answer.append("" + id_name[c_id] + "님이 나갔습니다.")

    
    return answer
