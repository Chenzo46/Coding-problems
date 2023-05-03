class student:
    def __init__(self, info):
        self.info = info

        split_info = self.info.split(':')
        self.name = split_info[0]
        self.stats = split_info[1].split(',')

    def get_gpa(self):
        pass

    def calculate_points(self):
        grade_points = 0
        credit_hours = 0
        for grade in self.stats:
            grade_points += (-ord(grade[0]) + 69) * int(grade[1])
            credit_hours += int(grade[1])


        return grade_points, credit_hours
    
    def get_gpa(self):
        grade_points, credit_hours = self.calculate_points()
        return grade_points / credit_hours

def main():

    cases = int(input())

    for case in range(cases):
        school_name = input()
        student_count = int(input())

        students = [student(input()) for _ in range(student_count)]

        students.sort(key = lambda x : x.get_gpa(), reverse = True)

        print(f'{school_name} = {students[0].name}')

if __name__ == '__main__':
    main()