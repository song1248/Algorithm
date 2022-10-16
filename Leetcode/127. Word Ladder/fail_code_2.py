from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # BFS 로 최단거리 찾는것이 빠를지 -> Memory Limit Exceeded
        # DFS 로 백트랙킹을한 완전탐색하는것이 빠를지
        #-> 이번엔 DFS
        
        wordList = set(wordList)
        answer = float('inf')
        len_wordList = len(wordList)
        flag = False
        def explore(word = beginWord, count = 0):
            nonlocal answer
            
            if word == endWord:
                answer = min(answer, count + 1)
                return
            
            if count == len_wordList or flag:
                flag == True
                return 0
                
            # 한글자 차이나고 사용하지 않았던 것으로 이동
            for i, tmp_word in enumerate(wordList):
                if not tmp_word:
                    continue
                word_gap = len(tmp_word)
                for j, ch in enumerate(word):
                    if ch == tmp_word[j]:
                        word_gap -= 1
                if word_gap == 1:
                    # tmp = wordList[i]
                    # wordList[i] = ''
                    wordList.remove(tmp_word)
                    explore(tmp_word, count + 1)
                    # wordList[i] = tmp
                    wordList.add(tmp_word)        
        explore()
        
        return 0 if answer == float('inf') else answer
