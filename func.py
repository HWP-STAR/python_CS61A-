def summation(n, term):
    total,k=0,1
    while k <=n:
        total,k=total+term(k),k+1
    return total
def cube(x):
    return x*x*x

def sum_cubes(n):
    return summation(n,cube)
print(f"Sum of cubes from 1 to 5: {sum_cubes(5)}")  # Example usage
print(f"1  to 3 sum of cubes: {sum_cubes(3)}")  # Example usage

def identity(x):
    return x

def sum_naturals(n):
    return summation(n, identity)

print(f"Sum of naturals from 1 to 100: {sum_naturals(100)}")  # Example usage

def pi_term(k):
    return 8 / ((4*k-3)*(4*k-1))

def pi_sum(n):
    return summation(n, pi_term)

#print(f"pi_sum(1e6):{pi_sum(1e6)}")  # Example usage
# 黄金分割
def improve(update,close,guess=10):
    while not close(guess):
        guess=update(guess)
    return guess

def golden_update(guess):
    return 1/guess+1
def square_close_to_successor(guess):
    return approx_eq(guess*guess,guess+1)
def approx_eq(x,y,tolerance=1e-5):
    return abs(x-y) < tolerance

phi=improve(golden_update,square_close_to_successor)
print(f"Golden ratio approximation: {phi}")  # Example usage

def jie(n):
    if n==1:
        return 1
    else:
        return n*jie(n-1)
    
def multiply(x,y):
    assert x>0 and y>0,"Both x and y must be positive integers."
    n=max(x,y)
    while True:
        if n%x==0 and n%y==0:
            return n
        n+=1

        