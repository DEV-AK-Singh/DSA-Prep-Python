def create_line(size, i=0):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    word = ''
    curr_size = size
    while curr_size > 0:
        word += chars[curr_size-1]
        curr_size -= 1
    start_word = list(word)[:size-i] #start word
    end_word = list(word[::-1])[1+i:] #end word  
    return '-'.join(start_word + end_word)

def print_rangoli(size):
    # your code goes here 
    width = len(create_line(size, 0))
    for i in range(size-1, 0, -1):
        print(create_line(size, i).center(width, '-'))
    for i in range(size):
        print(create_line(size, i).center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    