def allMatches(teams):
    assert len(teams) >= 2
    matches=[]
    for t1 in teams:
        for t2 in teams:
            if t1 != t2:
                m=(t1,t2)
                matches.append(m)
    return matches