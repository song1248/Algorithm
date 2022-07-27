def solution(n, build_frame):
    bo = [[0 for _ in range(n+1)] for _ in range(n+1)]
    pillar = [[0 for _ in range(n+1)] for _ in range(n+1)]
    # 보는
    def bo_rule(x, y):
        # 한쪽 끝 부분이 기둥 위에 있거나
        if pillar[y-1][x] == 1 or pillar[y-1][x+1] == 1:
            return True
        # 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
        if bo[y][x-1] == 1 and bo[y][x+1] == 1:
            return True
        return False
    
    # 기둥은 
    def pillar_rule(x, y):
        # 바닥 위에 있거나 
        if y == 0:
            return True    
        # 보의 한쪽 끝 부분 위에 있거나
        if bo[y][x] == 1 or bo[y][x-1] == 1:
            return True
        # 또는 다른 기둥 위에 있어야 합니다.
        if pillar[y-1][x] == 1:
            return True
        return False
    
    # build_type 0 은 기둥, 1은 보
    # d_or_c 0은삭제, 1은 설치
    def rule(x, y, build_type, d_or_c):
        # 보 설치
        if build_type and d_or_c:
            if bo_rule(x, y):
                bo[y][x] = 1
        # 기둥 설치
        elif not build_type and d_or_c:
            if pillar_rule(x, y):
                pillar[y][x] = 1
                
        # 보 삭제
        elif build_type and not d_or_c:
            bo[y][x] = 0
            # 기둥
            if pillar[y][x]:
                if not pillar_rule(x, y):
                    bo[y][x] = 1
            # 오른쪽 기둥
            if pillar[y][x+1]:
                if not pillar_rule(x+1, y):
                    bo[y][x] = 1
            # 오른쪽 보
            if bo[y][x+1]:
                if not bo_rule(x+1, y):
                    bo[y][x] = 1
            # 왼쪽 보
            if bo[y][x-1]:
                if not bo_rule(x-1, y):
                    bo[y][x] = 1        
        # 기둥 삭제
        else:
            pillar[y][x] = 0
            # 위의 기둥
            if pillar[y+1][x]:
                if not pillar_rule(x, y+1):
                    pillar[y][x] = 1
            # 위의 보
            if bo[y+1][x]:
                if not bo_rule(x, y+1):
                    pillar[y][x] = 1
            # 위의 왼쪽 보
            if bo[y+1][x-1]:
                if not bo_rule(x-1, y+1):
                    pillar[y][x] = 1
        
    for b_f in build_frame:
        x, y, build_type, d_or_c = b_f
        rule( x, y, build_type, d_or_c)
    
    answer = []
    for y in range(n+1):
        for x in range(n+1):
            if bo[y][x]:
                answer.append([x,y,1])
            if pillar[y][x]:
                answer.append([x,y,0])
        
#     for i in bo[::-1]:    
#         print(i)
#     for i in pillar[::-1]:    
#         print(i)
#     print("================================")
    return sorted(answer)
