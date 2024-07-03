# alist = []
# for i in {1,2,3,4,5,6}:
#     alist.append(i)
#     print(i)

# print(alist)

nestedlist = [
    [1,2,3],
    [3,4,5],
    [1,2,3]

]
nestedlist = [tuple(item) for item in nestedlist]

print(set(nestedlist))