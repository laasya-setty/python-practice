# Finding the Precentages
import functools
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks=student_marks.get(query_name)
    print(marks)
    result=functools.reduce(lambda a,b:a+b,marks)
    
print("{:.2f}".format(result/len(marks)))