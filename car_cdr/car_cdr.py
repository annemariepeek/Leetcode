def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(p):
    f = lambda x, y : x
    print(p(f))

def cdr(p):
    f = lambda x, y : y
    print(p(f))



car(cons(3,4))
cdr(cons(3,4))
