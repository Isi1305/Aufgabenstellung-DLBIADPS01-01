def naiveMatch(p,t): 
    if not p or not t: 
        return False 
    m = len(p) 
    n = len(t) 
    found = False 
    for i in range(n-m+1): 
        j = 0 
        k = i 
        while j < m and k < n and p[j] == t[k]: 
            j += 1 
        k += 1 
    if j == m: 
        found = True 
    return found 

def test_match_function(): 
assert naiveMatch('abc','aaaa') == False, "NoMatch failed" 