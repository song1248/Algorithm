def solution(n, k, cmds):
    
    # 현재 위치
    cur_point = k
    
    # dictionary 만들기
    name_dict = dict()
    for i in range(n):
        name_dict[i] = [i-1, i+1]
    # -1 을 범위 바깥임을 의미
    name_dict[n-1][1] = -1
    
    # 고유번호, 앞, 뒤
    deleted_stack = []    
    
    # 연산수행
    for cmd in cmds:
        # print(cur_point, name_dict)
        cmd = cmd.split(' ')
        if cmd[0] == 'U':
            for i in range(int(cmd[1])):
                cur_point = name_dict[cur_point][0]
        elif cmd[0] == 'D':
            for i in range(int(cmd[1])):
                cur_point = name_dict[cur_point][1]
                
        # 복구(현재 선택된 행은 바뀌지 않음)
        elif cmd[0] == 'Z':
            unq_num, prv_num, next_num = deleted_stack.pop()
            name_dict[unq_num] = [prv_num, next_num]
            if prv_num != -1:
                name_dict[prv_num][1] = unq_num
            if next_num != -1: 
                name_dict[next_num][0] = unq_num
            
            
        # 제거 후 바로 아래 행 선택, 선택된 행이 가장 마지막 행인 경우 바로 윗 행을 선택
        elif cmd[0] == 'C':
            # 앞 뒤의 값을 바꿔주고 제거
            prv_of_deleted, next_of_deleted = name_dict[cur_point]
            deleted_stack.append((cur_point, prv_of_deleted, next_of_deleted))
            
            if next_of_deleted != -1:
                name_dict[next_of_deleted][0] = prv_of_deleted
            
            if prv_of_deleted != -1:
                name_dict[prv_of_deleted][1] = next_of_deleted
                
            del name_dict[cur_point]
            cur_point = next_of_deleted if next_of_deleted != -1 else prv_of_deleted

    answer = ''
    for i in range(n):
        if i in name_dict:
            answer += 'O'
        else:
            answer += 'X'
    
    return answer
