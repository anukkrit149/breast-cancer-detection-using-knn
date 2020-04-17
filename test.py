def dynamicArray(n, queries):
    last_ans = 0
    res = list()
    sequences = [[] for i in range(n)]
    for query in queries:
        seq = ((query[1]^last_ans)%n)
        if query[0] == 2:
            last_ans= sequences[seq][(query[2]%len(query))]
            res.append(last_ans)
            print(last_ans)
        else:
            sequences[seq].append(query[2])
        return