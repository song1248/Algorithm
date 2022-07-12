# 유저가 탐험 할 수 있는 최대 던전 수 를 return 하라
import copy

def solution(k, dungeons):

    answer = -1
    
    def explore(n_explored_dungeon=-1, player=k, dungeons=dungeons):
        nonlocal answer
        n_explored_dungeon += 1

        # 갈 수 있는 dungeon이 있나 확인
        can_explore = False
        for i in range(len(dungeons)):
            if player >= dungeons[i][0]:
                can_explore = True
                dungeon = dungeons.pop(i)
                explore(n_explored_dungeon, player - dungeon[1], dungeons)
                dungeons.insert(i, dungeon)
        
        # 더이상 갈 수 있는곳이 없으면 종료
        if can_explore == False:
            answer = max(answer, n_explored_dungeon)
        
        return
    
    explore()
    
    return answer
