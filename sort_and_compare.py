def anagramSolution(s1, s2):
    # convert string to lists
    alist1 = list(s1)
    alist2 = list(s2)

    # sort each string alphabetically
    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    # check the length of each string AND the matches of characters 
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    
    return matches

print (anagramSolution('abcde', 'edcba'))