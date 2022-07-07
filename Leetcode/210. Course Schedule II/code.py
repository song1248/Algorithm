from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        
        # BFS방식을 이용(BFS는 아닌듯함,,)
        
        answer = []
        
        # index의 course를 듣기위해 충족시켜야 하는 list
        meet_list = [[] for i in range(numCourses)]
        for meet, prerequisite in prerequisites:
            meet_list[meet].append(prerequisite)
        
        # 시작 할 수 있는 course 찾아서 queue에 삽입
        queue = deque()
        for i in range(numCourses):
            if not meet_list[i]:
                queue.append(i)

        # 방문 체크 list
        visited = [0 for i in range(numCourses)]

        
        while queue:
            cur_course = queue.pop()
    
            # 모든 조건을 충족했으면 answer 에 append
            meet = True
            for i in meet_list[cur_course]:
                if visited[i] != 1:
                    meet = False
                    break
            if meet == False:
                continue
            
            
            answer.append(cur_course)
            visited[cur_course] = 1

            # 방문하지 않은 course를 queue에 삽입
            for next_course in range(numCourses):
                if visited[next_course] == 0:       
                    queue.append(next_course)      
            
            # 모든 강의를 들으면 answer return
            if visited.count(0) == 0:
                return answer
        # 모든 강의를 듣지 못하면 [] return
        return []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]] 
# numCourses = 2
# prerequisites = [[0,1]]
# numCourses = 100
# prerequisites = [[6,27],[83,9],[10,95],[48,67],[5,71],[18,72],[7,10],[92,4],[68,84],[6,41],[82,41],[18,54],[0,2],[1,2],[8,65],[47,85],[39,51],[13,78],[77,50],[70,56],[5,61],[26,56],[18,19],[35,49],[79,53],[40,22],[8,19],[60,56],[48,50],[20,70],[35,12],[99,85],[12,75],[2,36],[36,22],[21,15],[98,1],[34,94],[25,41],[65,17],[1,56],[43,96],[74,57],[19,62],[62,78],[50,86],[46,22],[10,13],[47,18],[20,66],[83,66],[51,47],[23,66],[87,42],[25,81],[60,81],[25,93],[35,89],[65,92],[87,39],[12,43],[75,73],[28,96],[47,55],[18,11],[29,58],[78,61],[62,75],[60,77],[13,46],[97,92],[4,64],[91,47],[58,66],[72,74],[28,17],[29,98],[53,66],[37,5],[38,12],[44,98],[24,31],[68,23],[86,52],[79,49],[32,25],[90,18],[16,57],[60,74],[81,73],[26,10],[54,26],[57,58],[46,47],[66,54],[52,25],[62,91],[6,72],[81,72],[50,35],[59,87],[21,3],[4,92],[70,12],[48,4],[9,23],[52,55],[43,59],[49,26],[25,90],[52,0],[55,8],[7,23],[97,41],[0,40],[69,47],[73,68],[10,6],[47,9],[64,24],[95,93],[79,66],[77,21],[80,69],[85,5],[24,48],[74,31],[80,76],[81,27],[71,94],[47,82],[3,24],[66,61],[52,13],[18,38],[1,35],[32,78],[7,58],[26,58],[64,47],[60,6],[62,5],[5,22],[60,54],[49,40],[11,56],[19,85],[65,58],[88,44],[86,58]]
Solution.findOrder(0, numCourses, prerequisites)
