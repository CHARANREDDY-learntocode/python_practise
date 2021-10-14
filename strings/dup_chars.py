from collections import Counter
def find_dup_chars(input):
    wc = Counter(input)
    print(list(wc.values()))

input='geeksforgeeks'
find_dup_chars(input)