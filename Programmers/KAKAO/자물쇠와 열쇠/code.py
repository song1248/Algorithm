import copy
def solution(key, lock):
    
    base_lock = lock
    # lock 배경만들기
    width = (len(key)-1)*2 + len(lock)
    lock = [ [ 0 for __ in range(width) ] for _ in range(len(key)-1) ] + [ [0]*(len(key)-1)+lck+[0]*(len(key)-1) for lck in lock ] + [ [ 0 for __ in range(width) ] for _ in range(len(key)-1) ]

    
    # key 만들기
    keys = []
    for _ in range(4):
        keys.append(key)
        key = list(zip(*key[::-1]))
        
    # 시작지점 i, j
    for i in range(len(lock)-len(key)+1):
        for j in range(len(lock[0])-len(key)+1):
            for key in keys:
                tmp_lock = copy.deepcopy(lock)
                break_point = False
                for u in range(len(key)):
                    for v in range(len(key[0])):
                        # key의 위치가 1 일때
                        if key[u][v] == 1:
                            # tmp_lock가 0 이면 / 1이면
                            if tmp_lock[i+u][j+v] == 0:
                                tmp_lock[i+u][j+v]+=1
                            else:
                                break_point = True           
                                break
                    if break_point == True:
                        break
                # key의 값을 다 입력했을때 lock이 다 1이면
                
                for a in range(len(key)-1, len(key)+len(base_lock)-1):
                    for b in range(len(key[0])-1, len(key[0])+len(base_lock[0])-1):
                        if tmp_lock[a][b] == 0:
                            break_point = True
                            break
                    if break_point == True:
                        break
                if break_point == False:
                    return True

    return False
