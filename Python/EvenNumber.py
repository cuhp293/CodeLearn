res = []
lengths = int(input())

for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)

def evenNum(res):
    ans = []
    for i in res:
        if i % 2 == 0:
            ans.append(i)
    print(ans)
evenNum(res)