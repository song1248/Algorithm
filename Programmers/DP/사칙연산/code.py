def solution(arr):
    min_value = 0
    max_value = 0
    
    # -를 지난 이후의 모든 값
    sum_value = 0
    for idx in range(len(arr)-1, -1, -1):
        
        # 덧셈일때는 아무것도 안함
        if arr[idx] == '+':
            continue
    
        # 뺄셈일때만
        elif arr[idx] == '-':
            
            # - 이전까지의 min값, max값
            tempmin = min_value
            tempmax = max_value
            
            # -(sum + max):-가 식전체에 붙는 경우, -sum+min:-가 이전 -값 앞까지만 붙는 경우
            min_value = min(-(sum_value + tempmax), -sum_value+tempmin)
            
            # -(sum + min):-가 식전체에 붙는 경우, -v+(sum-v)+max:-가 바로 뒤의 값에만 붙는 경우
            prv_val = int(arr[idx+1])
            
            max_value = max(-(sum_value+tempmin), -prv_val + (sum_value-prv_val) + tempmax)
            
            sum_value = 0
            
        # 숫자면
        else:
            sum_value += int(arr[idx])

        
    max_value += sum_value
    return max_value
