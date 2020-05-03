T = int(input("Enter the number of test cases: "))
while T!=0:
    m, n = map(int, input("Enter m and n: ").split())
    l, marked, p, g = [*range(2, n+1)], [], [], [*range(m, n+1)]
    for i in l:
        if i**2 in l:
            for j in l[l.index(i**2):]:
                if j%i == 0:
                    marked.append(j)
        else:
            break
    p = [x for x in g if (x not in marked) and x!=1]
    print("Prime Numbers are", p)
    T-=1