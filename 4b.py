def naiveMatch(p,t): 
    if not p or not t: 
        return 0 
    m = len(p) 
    n = len(t) 
    count = 0

    for i in range(n-m+1): 
        j = 0 
        k = i 
        while j < m and k < n and p[j] == t[k]: 
            j += 1 
            k += 1 
            if j == m: 
                count += 1
    return count 

def test_match_function(): 
    assert naiveMatch('abc','aaaa') == 0, "NoMatch failed" 
    assert naiveMatch('abc','abc') == 1, "SingleMatch failed"
    assert naiveMatch('abc','abcabc') == 2, "MultipleMatch failed"
    assert naiveMatch('abc','ababc') == 1, "PartialMatch failed"
    assert naiveMatch('','') == 0, "EmptyPatternAndText failed"