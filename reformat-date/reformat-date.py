class Solution:
    def reformatDate(self, date: str) -> str:
        month_dic ={"Jan" : "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        output = ''
        dd, mm, yyyy = date.split(' ')
        if int(dd[:-2]) <10 :
            output = yyyy + '-' + month_dic[mm] + '-0' + dd[:-2]
        else :
            output = yyyy + '-' + month_dic[mm] + '-' + dd[:-2]
        return output
