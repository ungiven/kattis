import sys

for i in sys.stdin:
    ab = i.split()
    if(len(ab)) == 3:
        _dist = int(ab[1])
        _m = int(ab[2])
        length = int(ab[0])
    elif(len(ab)) == length:
        _li = list(map(int, ab))


#_dist = 2
#_m = 1
# _li= '1 3 5 7 9 11 13'
# _li= '1 2 4 6 7 9 10 11'
#_li = '1 7 8 2 6 4 3 5'
#_li = list(map(int, _li.split()))

_mem = {}
sys.setrecursionlimit(10000)

# find candidates
def possi(index, v, li):
    r = []

    for i in range(-_dist, _dist+1):
        if index + i >= 0 and index + i < len(li) and i != 0:
            if index + i not in v and abs(li[index] - li[index + i]) <= _m:
                r.append(index + i)

    return r


# list forward candidates
def fcand(index):
    r = set()
    p = possi(index, [], _li)

    for i in range(1, _dist+1):
        if index+i in p:
            r.add(index+i)

    return r

# find isolates
def isolate(li):
    start = 0
    count = 0
    iso = []

    for i in range(len(li)):
        if not possi(i, [], li):
            count += 1

        else:
            if count >= _dist or count == i:
                tmp = li[start:i-count]
                if tmp:
                    iso.append(li[start:i-count])
                start = i
            count = 0

    iso.append(li[start:len(li)-count])

    return iso

# calculate path from index
def path(index, li, v=[]):
    v = v[:]
    v.append(index)
    p = possi(index, v, li)

    if tuple(sorted(v)) in _mem:
        return _mem[tuple(sorted(v))]
    if not p:
        return 0

    r = [1+path(i, li, v) for i in p]

    # return max(r)

    _mem[tuple(sorted(v))] = max(r)
    return _mem[tuple(sorted(v))]


def run(lol):
    if len(_li) < 2:
        return len(_li)

    r = []

    for li in lol:
        for i in range(len(li)):
            r.append(1+path(i, li))
        _mem.clear()

    return max(r)


if __name__ == '__main__':
    # Generate sublists
    iso = isolate(_li)

    print(run(iso))
    # print(iso)
