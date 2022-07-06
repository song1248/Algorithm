from collections import deque
def solution(begin, target, words):
    
    # 단어들간의 차이를 반환하는 함수
    def distance(w1, w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
        return count

    count = 0
    # 방문한 word를 재방문하지 않기위해 deque를 이용
    words = deque(words)
		# BFS를 이용한 탐색을 위해 queue를 이용
		queue = deque([begin])
    # queue 가 빌때까지( = 모든 값을 탐색할때까지)
    while queue:
        # que의 값을 하나 뽑아서 비교하는 기준단어로 설정
        default = queue.pop()
				# traget과 같은다어를 찾으면 count를반환하고 종료
        if distance(default,target)==0:
            return count
        # 단어와의 거리를 비교하여 distance가 1인값만 queue에 append
        for _ in range(len(words)):
            word = words.popleft()
            if distance(default, word) == 1:
                queue.append(word)
            else:
                words.append(word)
				# 넓이탐색을 한번 진행할때마다 count +=1
        count += 1
        
    # distance가 0인것을 찾지 못하면 0을 반환    
    return 0
