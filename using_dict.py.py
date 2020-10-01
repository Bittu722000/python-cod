def NotMe(inp, start, end):
    lis = []
    for i in inp:
        if i<start or i>end:
            lis.append(i)
    return lis


inp=list(range(1,11))
start=int(input("Enter start"))
end=int(input("Enter end"))
print(NotMe(inp, start , end))

    