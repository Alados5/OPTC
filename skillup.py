def fact(i):
    """
    Returns the factorial of the given number i
    """
    prod=1
    for j in range(1, i+1):
        prod*=j
    return prod


def f(k, n, p):
    """
    Calculates de probability of getting exactly k successes in a
    Binomial distribution X=B(n,p)
    f = Pr(X=k) = (n k) * p**k * (1-p)**(n-k)
    (n k) = n!/(k!*(n-k)!)
    """

    nf = fact(n)
    kf = fact(k)
    nkf = fact(n-k)
    combi = nf/(kf*nkf)

    pro1 = p**k
    pro2 = (1-p)**(n-k)
    
    prob = combi * pro1 * pro2

    return prob
    
def F(k, n, p):
    """
    Returns the cumulative probability F=Pr(X<=k)
    """
    sum = 0
    for i in range(k+1):
        bini = f(i, n, p)
        sum += bini

    return sum

def R(k, n, p):
    """
    Returns the remaining probability R=Pr(X>=k)
    R = Pr(X>(k-1)) = 1-Pr(X<=(k-1))
    """
    return 1-F(k-1, n, p)


def Lv(k, n, event=True, japan=False):
    """
    Probability of getting k skillups with n copies, with event or not.
    Has a p = 1/10 for Global and p = 1/6 for Japan without skillup Event.
    """
    if japan == False:
        if event == True:
            return R(k, n, 0.2)
        else:
            return R(k, n, 0.1)

    else:
        if event == True:
            return R(k, n, 0.333)
        else:
            return R(k, n, 0.166)

def LvOC(k, n, event=True, japan=False):
    """
    Same as Lv but with Online Calculator probabilities (0.125 & 0.2)
    """
    if japan == False:
        if event == True:
            return R(k, n, 0.25)
        else:
            return R(k, n, 0.125)

    else:
        if event == True:
            return R(k, n, 0.4)
        else:
            return R(k, n, 0.2)   


def N(k, x=0.75, event=True):
    """
    Calculates the number N of copies needed to get k or more successes
    (skillups) with a probability x (at 75% by defect). 
    The last parameter indicates if the probability p is with
    Skillup x2 event (True) or not (False).
    or without it

    f = Pr(X=k) = (n k) * p**k * (1-p)**(n-k)
    (n k) = n!/(k!*(n-k)!)

    R = Pr(X>=k) = x = SUM ( f_k + ... + f_n )
    
    """

    n = 1
    while n<200:
        t = Lv(k, n, event)

        if t >= x:
            break

        n+=1

    return n
            

def NOC(k, x=0.75, event=True):
    """
    Same as function N, but with the probability values of the
    Online Calculator at optc-db.github.io
    p=0.125, and not my theoretical p=0.1
    Basically calls the function LvOC instead of Lv
    """

    n = 1
    while n<200:
        t = LvOC(k, n, event)

        if t >= x:
            break

        n+=1

    return n
