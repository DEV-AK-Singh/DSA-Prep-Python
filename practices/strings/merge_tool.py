def req_word(substring):
    word = []
    for i in substring:
        if i not in word:
            word.append(i)
    return "".join(word)

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(req_word(string[i:i+k]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)