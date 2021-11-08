import itertools

def get_cartesian_product(a, b):
    return list(itertools.product(a,b))

print(get_cartesian_product([1, 2], [3, 4])) # [(1, 3), (1, 4), (2, 3), (2, 4)]

def get_permutations(s, n):
    return list(map(lambda x: ''.join(x), itertools.permutations(sorted(s), n)))

print(get_permutations("cat", 2)) # ["ac", "at", "ca", "ct", "ta", "tc"]

def get_combinations(s, n):
    out = []
    for k in range(1,n+1):
        out.extend(list(map(lambda x: ''.join(x), itertools.combinations(sorted(s), k))))
    return out

print(get_combinations("cat", 2)) # ["a", "c", "t", "ac", "at", "ct"]

def get_combinations_with_r(s, n):
    return list(map(lambda x: ''.join(x), itertools.combinations_with_replacement(sorted(s), n)))
    
print(get_combinations_with_r("cat", 2)) # ["aa", "ac", "at", "cc", "ct", "tt"]


def compress_string(s):
    return list(itertools.groupby(s

compress_string('1222311') == [(1, 1), (3, 2), (1, 3), (2, 1)]

def maximize(lists, m):
    raise RuntimeError("Not implemented")

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]