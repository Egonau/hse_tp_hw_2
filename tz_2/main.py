def _min(arr):
    minn = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < minn:
            minn = arr[i]
    return minn


def _max(arr):
    maxx = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maxx:
            maxx = arr[i]
    return maxx


def _sum(arr):
    summ = 0
    for i in arr:
        summ += i
    return summ


def _mult(arr):
    mult = 1
    for i in arr:
        mult *= i
    return mult


def file_reader(name):
    f = open(name, 'r')
    a = f.read()
    return list(map(int, a.split(" ")))


