def is_even_vowel(word):
    count = 0
    flag = False
    for letter in word:
        if letter in ['a','e','i','o','u','y']:
            count += 1
        else:
            continue   
    if count % 2 == 0:
        flag = True
    return flag

def score_words(words):
    score = 0
    for word in words:
        if is_even_vowel(word):
            score += 2
        else:
            score += 1   
    return score 

n = int(input())
words = input().split()
print(score_words(words))