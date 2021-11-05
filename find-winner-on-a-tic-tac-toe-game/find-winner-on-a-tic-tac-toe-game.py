class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        bingo = [['', '', ''],
            ['', '', ''],
            ['', '', '']]

        count = 0
        for move in moves:
            if count %2 == 0:
                bingo[move[0]][move[1]] = 'A'
            else :
                bingo[move[0]][move[1]] = 'B'
            count +=1    
        for i in range(3):
            s = ''
            for j in range(3):
                s+= bingo[i][j]
            if s == 'AAA':
                return 'A'
            elif s == 'BBB':
                return 'B'

        for i in range(3):
            s = ''
            for j in range(3):
                s+= bingo[j][i]
            if s == 'AAA':
                return 'A'
            elif s == 'BBB':
                return 'B'

        s1 = bingo[0][0] + bingo[1][1] + bingo[2][2]
        s2 =bingo[0][2] + bingo[1][1] + bingo[2][0]
        if s1 == 'AAA' or s2 == 'AAA':
            return 'A'
        elif s1 == 'BBB'or s2 == 'BBB':
            return 'B'

        for l in bingo:
            if '' in l:
                return 'Pending'
        return 'Draw'