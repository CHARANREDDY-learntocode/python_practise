sentence = input('Enter the sentence: ')

#print(sentence.split()[::-1])
lst = sentence.split()
print(' '.join(lst[::-1]))
