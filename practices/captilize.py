# Complete the solve function below.
def solve(s):
    input_string=list(map(str,s.split()))
    result_string=s
    for i in input_string:
        result_string = result_string.replace(i,i.capitalize())
    return result_string 

if __name__ == '__main__': 
    s = input()
    result = solve(s) 
    print(result)
