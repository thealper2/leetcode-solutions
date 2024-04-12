from typing import List

def hIndex(citations: List[int]) -> int:
    citations.sort()
    h = len(citations)
    for i in citations:
        if i < h:
            h = h - 1

    #print(h)
    return h
