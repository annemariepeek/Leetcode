def longest_sub(s, k):
    max = ""
    for i in range(len(s)):
        ret = ""
        sett = set()
        for j in range(i, len(s)):
            if s[j] in sett:
                ret += s[j]
            else:
                if len(sett) < k:
                    ret += s[j]
                    sett.add(s[j])
                else: 
                    if len(ret) > len(max):
                        max = ret
                    break 

    return max

print(longest_sub("abcba", 2))


#  i in s? 
#  y -> append to a, next iteration
#  n -> len(s) < k then appendto a and add i to s
#  n -> done reset 

