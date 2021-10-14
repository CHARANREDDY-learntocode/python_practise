def armstrong(num):
    temp = num
    sum = 0
    while (temp!=0):
        r = temp%10
        sum += pow(r, len(str(num)))
        temp = temp//10
    if sum == num: print('yes')
    else: print('no')
armstrong(153)