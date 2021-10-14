lst = [['Hello', 'hope', 'are'], ['charan', 'you', 'good']]

rez = []
#new_lst = [' '.join([lst[i][i+1] for j in range(len(lst[0]))]) for i in range(len(lst)-1)]
for i in range(len(lst[0])):
    temp_list = []
    for j in range(len(lst)):
        temp_list.append(lst[j][i])
    rez.append(' '.join(temp_list))

print(rez)

print(' '.join(('hello', 'haii')))

print([' '.join(ele) for ele in list(zip(*lst))])