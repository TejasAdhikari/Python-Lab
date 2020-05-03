T = int(input("Enter the number of test cases: "))
while T!=0:
    m, n = map(int, input("Enter m and n: ").split())
    l, marked, p = [*range(m, n+1)], [], []
    for i in l:
        if (i**2 in l) and i!=1:
            for j in l[l.index(i**2):]:
                if j%i == 0:
                    marked.append(j)
        elif i==1:
            continue
        else:
            break
    p = [x for x in l if (x not in marked) and x!=1]
    print("Prime Numbers are", p)
    T-=1