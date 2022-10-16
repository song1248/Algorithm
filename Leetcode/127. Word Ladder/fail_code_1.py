from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # BFS 로 최단거리 찾는것이 빠를지 -> Memory Limit Exceeded
        # DFS 로 백트랙킹을한 완전탐색하는것이 빠를지
        #-> 일eks BFS
        
        wordList = set(wordList)
        
        Q = deque([[beginWord, 0 ,wordList]])
        
        
        while Q:
            
            cur_word, count ,wordList= Q.popleft()
            
            if cur_word == endWord:
                return count + 1
            
            if not wordList:
                continue
                
            # 한글자 차이나고 사용하지 않았던 것으로 이동
            for i, tmp_word in enumerate(wordList):
                word_gap = len(tmp_word)
                for j, ch in enumerate(cur_word):
                    if ch == tmp_word[j]:
                        word_gap -= 1
                if word_gap == 1:
                    copied_wordlist = wordList.copy()
                    copied_wordlist.remove(tmp_word)
                    Q.append([tmp_word, count+1, copied_wordlist])
        
        return 0
