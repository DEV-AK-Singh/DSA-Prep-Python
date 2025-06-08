import re 
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    string = str(input()) 
    # res = -1
    # for i in range(1, len(string)):
    #     if string[i-1].isalnum():
    #         if string[i-1] == string[i]:
    #             res = string[i]
    #             break
    #         else:
    #             pass  
    #     else:
    #         pass    
    # print(res)   

    grps = re.findall(r"([a-zA-Z0-9])\1{1}", string)
    print(grps[0] if grps else -1)