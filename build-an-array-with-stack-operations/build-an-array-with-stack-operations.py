class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        start =1
        for num in target :
            for i in range(start, n+1) :
                if num == i :
                    output.append("Push")
                    start =i+1
                    break
                else :
                    output += ["Push", "Pop"]

        return output
