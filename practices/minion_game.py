def substrings(s):
    words = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            words.append(s[i:j])
    return words

def count_word_presence(words, substring):  
    return words.count(substring)

def is_vowel(word):
    char = word[0]
    return char in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

def minion_game(string):
    all_words = substrings(string)
    unique_words = list(set(all_words))
    stuart = 0
    kevin = 0
    for word in unique_words: 
        if is_vowel(word):
            kevin += count_word_presence(all_words, word) 
        else:
            stuart += count_word_presence(all_words, word) 
    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)