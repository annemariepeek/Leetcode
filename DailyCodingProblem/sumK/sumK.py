def sumK (k, list):

    for i in range(0, len(list)):
        for j in range(1, len(list)):
            if list[i]+list[j] == k:
                return True
    return False


def sumK_bonus (k, list):


    for i in range(1,len(list)):
        a = list
        a = [x+list[i] for x in a]
        print(a)
        if a.count(k) != 0 and a[i] != k: 
            return True

    return False



print(sumK_bonus(6, [10,15,3,7]))







# 10 5 3 7 | 10 5 3 7 | 10 5 3 7 | 10 5 3 7 