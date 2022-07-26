
def solution(stones, k):
    # n보다 작은수가 연속으로 있는지 확인
    # 이분탐색
    start_point = 0
    end_point = 200000000
    middle_point = int((start_point+end_point)/2)
    while start_point != middle_point:
        print(middle_point)
        count = 0
        prev_val = 1
        for stone in stones:
            if stone - middle_point <=0:
                count += 1
            else:
                count = 0
            if count>=k:
                break
                
        if count>= k:
            end_point = middle_point
        else:
            start_point = middle_point

        # 소숫점이하 버림
        middle_point = int((start_point+end_point)/2)
    return middle_point + 1
