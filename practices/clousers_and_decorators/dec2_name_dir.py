import operator

def person_lister(f):
    def inner(people):
        sorted_list = sorted(people, key=operator.itemgetter(2))
        return map(f, sorted_list)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')