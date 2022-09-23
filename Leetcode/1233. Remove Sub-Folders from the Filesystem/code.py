class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
            
            
        f_dict = {}
        
        for f_str in folder:
            base_dict = f_dict
            f_list = f_str.split('/')[1:]
            for i, file in enumerate(f_list):
                file = '/' + file
                if file not in base_dict:
                    base_dict[file] = {}
                if i == len(f_list)-1:
                    base_dict[file] = {'1':0}
                
                base_dict = base_dict[file]
                
        answer = []
        def explore(base_dict = f_dict , path = ''):
            nonlocal answer
            
            # falg 가 있으면
            if '1' in base_dict:
                answer.append(path)
                return
            
            for key in base_dict.keys():
                explore(base_dict[key], path + key )
                
        explore()
        
        return answer
