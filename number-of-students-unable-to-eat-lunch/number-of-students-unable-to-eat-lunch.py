class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            s = students.pop(0)
            if s == sandwiches[0] :
                sandwiches.pop(0)
            else :
                students.append(s)

            if len(students) == 0:
                break
            if sandwiches[0] not in students :
                break
        return len(students)