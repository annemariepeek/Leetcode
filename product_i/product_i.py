def product_i(l):

    a = []

    for i in range(0, len(l)):
        product = 1
        for j in range (0,len(l)):
            if j != i:
                product *= l[j]
    
        
        a.append(product)
    
    return a

def product_i2(l):
    a = []

    product = 1 
    for i in range(0, len(l)):
        product *= l[i]
    
    for i in range(0,len(l)):
        a.append(int (product/l[i]))

    return a





print(product_i([1, 2, 3, 4, 5]))
print(product_i([3, 2, 1]))

print(product_i2([1, 2, 3, 4, 5]))
print(product_i2([3, 2, 1]))
