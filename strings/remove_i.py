word = input('Enter a sentence: ')
place = int(input(''))

print(''.join([word[i] for i in range(len(word)) if i!=place]))