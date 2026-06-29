# Discussion 1 问题讨论
#Q1
def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(7)
    True
    >>> is_prime(9)
    False
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    k=2
    while k < n:
        if n % k == 0:
            return False
        k +=1
    return True

# Q2
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    k= 1
    while k <= n:
        if k % 3 == 0 and k % 5 == 0:
            print('fizzbuzz')
        elif k % 3 == 0:
            print('fizz')
        elif k % 5 == 0:
            print('buzz')
        else:
            print(k)
        k += 1
#Q3
def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """
    "*** YOUR CODE HERE ***"
    if x < 10:
        return True
    else:
        last = x % 10
        second_last = (x // 10) % 10
        if last < second_last:
            return False
        x = x // 10
        return ordered_digits(x) # 使用递归来检查剩余的数字是否有序