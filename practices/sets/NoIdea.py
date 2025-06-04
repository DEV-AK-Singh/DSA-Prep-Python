# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    happiness_score = 0
    m, n = input().split()
    arr = map(int, input().split())
    A_set = set(map(int, input().split()))
    B_set = set(map(int, input().split())) 
    for ele in arr:
        if ele in A_set:
            happiness_score += 1
        elif ele in B_set:
            happiness_score -= 1
        else:
            pass
    print(happiness_score)        
