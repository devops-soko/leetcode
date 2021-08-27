import datetime
class Solution:
    def reformatDate(self, date: str) -> str:
        month_dic ={"Jan" : 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
        dd, mm, yyyy = date.split(' ')
        x= datetime.datetime(int(yyyy), month_dic[mm], int(dd[:-2]))
        return x.strftime("%Y-%m-%d")