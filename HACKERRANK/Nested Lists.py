
import copy
if __name__ == '__main__':
    main = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        main.append((name, score))

    marks = sorted(set([x[1] for x in main]))
    second = marks[1]
    temp = sorted(main)
    for i in temp:
        if second == i[1]:
            print(i[0])
        
    