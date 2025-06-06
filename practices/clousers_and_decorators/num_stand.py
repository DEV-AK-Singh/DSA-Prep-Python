def wrapper(f):
    def fun(l):
        nums = []
        for i in l:
            if len(i) == 10:
                nums.append(f"+91 {i[0:5]} {i[5:]}")
            elif len(i) == 11:
                nums.append(f"+91 {i[1:6]} {i[6:]}")
            elif len(i) == 12:
                nums.append(f"+91 {i[2:7]} {i[7:]}") 
            else:
                nums.append(f"+91 {i[3:8]} {i[8:]}")    
        return f(nums)     
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 