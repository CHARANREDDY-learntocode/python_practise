def is_symmetric(word):
    length = len(word)
    if length%2 == 0: mid = length//2
    else: mid = (length//2)+1
    start1 = 0
    start2 = mid

    while (start1 < mid and start2 < length):
        if word[start1] != word[start2]:
            return False
        start2+= 1
        start1+=1
    return True

word = input('Enter a word: ')

print('symmetric') if is_symmetric(word) else print('Not Symmetric')