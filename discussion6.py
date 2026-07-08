# Q1
def gen_fib():
    n,add=0,1
    while True:
        yield n
        n,add = n+add,n

# Q2
def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    t_list=list(t)
    for i in range(len(t_list)-1):
        yield t_list[i+1]-t_list[i]
