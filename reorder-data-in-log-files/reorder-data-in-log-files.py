class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_list, dig_list = [], []
        for log in logs :
            if (''.join(log.split(' ')[1:])).isdigit() :
                dig_list.append(log)
            else : 
                let_list.append(log.split(' '))

        let_list = sorted(let_list, key=lambda x: (x[1:], x[0]))
        for i,v in enumerate(let_list)  :
            let_list[i] = ' '.join(v)
        return let_list + dig_list