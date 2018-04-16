import copy

def combine(l, n):
    answers = []
    one = [0] * n
    def next_c (li = 0, ni = 0):
        if ni == n:
            # if sum(one) == 150:
            answers.append(copy.copy(one))
            return
        for lj in range(li, len(l)):
            one[ni] = l[lj]
            next_c(lj, ni + 1)
    next_c()
    return answers

# n为要分的批次，begin和end代表Zn取值的区间
def createData(n, begin = 0, end = 51):
    # 创建从Begin到end的列表
    li = [i for i in range(begin, end)]
    lis = combine(li,n)
    for i in range(0, len(lis)):
    #     if i%5 == 0 and i != 0:
    #         print()
    #     print(lis[i],end=",")
    # print("count = %d" % len(lis))
        print(lis[i])
    print("count = %d" % len(lis))

li = [9,0,23,34,545]
print(li)


