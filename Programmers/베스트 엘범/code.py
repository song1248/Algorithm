# 노래수록기준
# - 가장 많이 재생된 노래를 두 개
# - 노래가 많이 재생된 장르
# - 장르 내에서 많이 재생된 노래
# - 장르 내에서 재생횟수가 같은 노래중에서는 고유번호가 낮은 노래를 먼저 수록
# - 고유번호를 순서대로 return

# O(4N)

from collections import defaultdict
def solution(genres, plays):
    
    # 장르마다 고유 많이 재생된 장르 순으로 idx붙이기
    gen_count_dict = defaultdict(int)
    # album에 담긴 수 count
    alubm_genre_count = defaultdict(int)
    
    # 재생횟수 세기
    for i, genre in enumerate(genres):
        gen_count_dict[genre] += plays[i]
    
    # 엘범 list 만들기
    album_list = []
    for i, play in enumerate(plays):
        g_idx = gen_count_dict[genres[i]]
        album_list.append([g_idx, play, i])
    
    # 정렬하고, 2개이하씩 answer에 담기
    answer = []
    for genre, play, idx in sorted(album_list, key = lambda x : (-x[0], -x[1], x[2])):
        if alubm_genre_count[genre] < 2:
            alubm_genre_count[genre] += 1
            answer.append(idx)
    
    return answer
