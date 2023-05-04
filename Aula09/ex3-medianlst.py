def median(lst):
    assert len(lst) > 0
    srtlst = sorted(lst)
    if len(lst)%2 == 0: #se lista é par
        spot2 = len(lst) / 2
        spot1 = spot2-1
        m = (srtlst[int(spot1)] + srtlst[int(spot2)]) / 2
    else: #se impar
        spot = (len(lst) - 1) / 2
        m = srtlst[int(spot)]
    return m

def check(lst):
    backup = lst. copy()
    m = median(lst)
    return m, lst