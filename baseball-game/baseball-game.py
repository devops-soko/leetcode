class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for v in ops :
            if v == 'D':
                result.append(result[-1] *2)
            elif v == 'C':
                result.pop()
            elif v == '+':
                result.append(result[-2] + result[-1])
            else:
                result.append(int(v))
        return sum(result)