class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dic = ['/']
        for log in logs :
            if log == './':
                next
            elif log == '../' :
                if len(dic) != 1 :
                    dic.pop()
            else:
                dic.append(log)
        return len(dic) -1