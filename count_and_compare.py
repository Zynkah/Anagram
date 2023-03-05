def anagramSolution(s1, s2):
    c1 = [0]*26
    c2 = [0]*26

    # counts the number of times each character occurs
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j < 26 and stillOK:
        # compares the two lists of counts
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK


print(anagramSolution('apple', 'pleap'))
