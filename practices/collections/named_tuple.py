from collections import namedtuple
if __name__ == "__main__": 
    n = int(input())
    fields = list(map(str, input().split()))
    Student = namedtuple('student', ",".join(fields))
    records = []
    for _ in range(n):
        records.append(Student(*input().split()))
    marks = [int(s.MARKS) for s in records] 
    avg = sum(marks) / len(marks)
    print(f"{avg:.2f}")
    