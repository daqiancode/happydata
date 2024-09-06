from typing import List, Dict, Iterable, Generator, Callable


def groupby(l: Iterable, key: str) -> Dict:
    d = {}
    for item in l:
        k = item[key]
        if k not in d:
            d[k] = []
        d[k].append(item)
    return d

def groupby_fn(l: Iterable, fn: callable) -> Dict:
    d = {}
    for item in l:
        k = fn(item)
        if k not in d:
            d[k] = []
        d[k].append(item)
    return d

def unique(l:List) -> List:
    """unique list and keep order"""
    seen = set()
    return [x for x in l if not (x in seen or seen.add(x))]


def partition(l: Iterable,partition_size:int) -> Generator[List, None, None]:
    """Partition a list into partitions of size partition_size"""
    if l is None:
        return
    cur = []
    i = 0
    for v in l:
        cur.append(v)
        i += 1
        if i == partition_size:
            yield cur
            cur = []
            i = 0
    if cur:
        yield cur

def divide(l: List, num_partitions:int) -> List[List]:
    """Partition a list into num_partitions partitions"""
    if l is None:
        return []
    partition_size = len(l)//num_partitions
    if partition_size == 0:
        partition_size = 1
    elif len(l) % num_partitions != 0:
        partition_size += 1
    return [l[i*partition_size : (i+1) * partition_size] for i in range (num_partitions)]