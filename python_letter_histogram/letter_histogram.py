def letter(word):

    letter_count = {}
    for char in word:
        letter_count[char] = letter_count.get(char,0) + 1
    return letter_count


usr_inp = input('Please enter a word')

print(letter(usr_inp))