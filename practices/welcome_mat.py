def mat_pattern(M, N): 
    pat = ".|."
    name = "welcome"
    center = M//2
    max_pattern = M-2
    for i in range(0, M): 
        if i < center:
            pattern = pat * (2 * i + 1) 
            print(pattern.center(N, "-"))  
        elif i == center:
            print(name.center(N, "-"))
        else:
            pattern = pat * (max_pattern - 2 * (i - center - 1))
            print(pattern.center(N, "-")) 

if __name__ == "__main__":
    M, N = input().split()
    M = int(M)
    N = int(N)
    mat_pattern(M, N)