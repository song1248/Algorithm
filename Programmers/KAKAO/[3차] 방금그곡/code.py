# 음악의 첫부분과 끝부분이 이어진 맬로디일 수있음
# 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다.
# 네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교
# 음악의 제목을 구하여라.

#  음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공
# 네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개
# 각 음은 1분에 1개씩 재생
# 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
# 음악이 00:00를 넘겨서까지 재생되는 일은 없다.
# 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
# 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다

def solution(m, musicinfos):
    answer = []
    
    m = m.replace('C#', 'c', len(m))
    m = m.replace('D#', 'd', len(m))
    m = m.replace('F#', 'f', len(m))
    m = m.replace('G#', 'g', len(m))
    m = m.replace('A#', 'a', len(m))
    
    for idx, item in enumerate(musicinfos):

        s_t, e_t, title, melody = item.split(',')
        
        melody = melody.replace('C#', 'c', len(melody))
        melody = melody.replace('D#', 'd', len(melody))
        melody = melody.replace('F#', 'f', len(melody))
        melody = melody.replace('G#', 'g', len(melody))
        melody = melody.replace('A#', 'a', len(melody))
        
        s_h, s_m = s_t.split(':')
        e_h, e_m = e_t.split(':')
        s_t = int(s_h) * 60 + int(s_m)
        e_t = int(e_h) * 60 + int(e_m)
        len_music = e_t - s_t
        
        music = ''
        for i in range(len_music):
            music += (melody[i % len(melody)])
    
        if m in music:
            answer.append([len_music, idx, title]) 
   
    answer.sort(key = lambda x : (-x[0], idx))
    
    return answer[0][-1] if answer else '(None)'
