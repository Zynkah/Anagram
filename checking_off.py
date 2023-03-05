def anagramSolution1(s1,s2):
    # check the lengths of the strings, if they are NOT equal then false
    if len(s1) != len(s2):
        stillOK = False

    # strings are immutable, first step will be to convert the second string to a list
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            # check if letter is in same position for each
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                # pass through the characters in s2
                pos2 = pos2 + 1

        if found:
            # checking off a character will be accomplished by replacing it with the special Python Value None
            alist[pos2] = None
        else:
            stillOK = False
        # pass through the characters in s1
        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('abcd','dcba'))