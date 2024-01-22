def nonrepeat(string):
    freq = {}
    for x in string:
        # we are getting the value of the string then increamenting it along the way it happens to occur again in the string
        freq[x] = freq.get(x, 0) + 1

    for i in string:
        if freq[i] == 1:
            return i
    return -1

print(nonrepeat('abcdabcef'))


