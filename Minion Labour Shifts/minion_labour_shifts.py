def answer(data, n):
    data_set = set(data)
    for d in data_set:
        if data.count(d) > n:
            data = filter(lambda a: a != d, data)
    return data

data=[1,2,2,3,3,3,4,5,5]
n=1
print answer(data,n)
