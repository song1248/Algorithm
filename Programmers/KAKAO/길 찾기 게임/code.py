# 파이썬 재귀 limit이 1000이기 때문에 재귀 limit을 늘려주어야 한다

import sys
sys.setrecursionlimit(10**6)


def solution(nodeinfo):
    
    # index 붙이고 정렬
    new_nodeinfo = []
    for i,  coordinate in enumerate(nodeinfo):
        new_nodeinfo.append(coordinate + [i+1])
        
    nodeinfo = sorted(new_nodeinfo)
    
    # 전휘순회 list, 후위순회 list
    preorder_list=[]
    postorder_list = []

    # 순회
    def explore(explore_type, nodeinfo=nodeinfo):
        nonlocal preorder_list
        nonlocal postorder_list
        
        if not nodeinfo:
            return
        
        # 가장 높은 layer의 x값찾기
        cur_y = 0
        for x, y, num in nodeinfo:
            cur_y = max(cur_y, y)
        
        # 중간값, 현재 node의 idx구하기
        cur_x = 0
        cur_num = 0
        cur_i = 0
        for i, coordinate in enumerate(nodeinfo):
            cur_i = i
            cur_x = coordinate[0]
            tmp_y = coordinate[1]
            cur_num = coordinate[2]
            if tmp_y == cur_y:
                break
        
        # 오른쪽 왼쪽 나누기
        right_nodeinfo = nodeinfo[cur_i+1:]
        left_nodeinfo = nodeinfo[:cur_i]
        
        
        # 탐색
        if explore_type == 'preorder':
            # value 추가
            preorder_list.append(cur_num)
            # 왼쪽 탐색
            explore('preorder', left_nodeinfo)
            # 오른쪽 탐색
            explore('preorder', right_nodeinfo)           
        
        # 탐색
        if explore_type == 'postorder':
            # 왼쪽 탐색
            explore('postorder', left_nodeinfo)
            # 오른쪽 탐색
            explore('postorder', right_nodeinfo)
            # value 추가
            postorder_list.append(cur_num)
   
    explore('preorder')
    explore('postorder')
    return [preorder_list, postorder_list]
