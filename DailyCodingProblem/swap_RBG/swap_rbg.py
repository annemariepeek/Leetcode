def swap_rgb(a):

    c = ''

    for i in range(0, len(a)):
        c = a[i]
        if c == 'R':
            a.pop(i)
            a.insert(0,c)
            
            print(i, "in R")
            print(a)
            i -= 1
        elif c == 'B':
            
            a.pop(i)
            a.append(c)
            i -= 1
            print(i, "in B")
            print(a)
            


    
    return a 






a = ['B', 'G', 'B', 'R', 'R', 'B', 'R', 'G']
print(swap_rgb(a))

# ['R', 'R', 'R', 'G', 'G', 'B', 'B']

# a = ['R', 'R', 'R', 'G', 'G', 'B', 'B',]

