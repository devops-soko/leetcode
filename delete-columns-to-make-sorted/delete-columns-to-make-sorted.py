class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        s_len= len(strs[0])
        result =['' for i in range (s_len)]
        for str in strs :
            for i in range(s_len) :
                result[i] = result[i] + str[i]
        count =0
        for str in result:
            if str != ''.join(sorted(str)):
                count += 1
        return count