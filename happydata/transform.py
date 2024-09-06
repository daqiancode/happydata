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