# 递归函数学习

# 计算所有数字和
def sum_digits(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        return last_digit + sum_digits(n // 10)
# 计算阶乘
def fact_iter(n):
    assert n > 0, "n must be a positive integer."
    if n == 1:
        return 1
    else:
        return n * fact_iter(n - 1)
    
def fact_k(n,k):
    if k == 1:
        return n
    else:
        return n * fact_k(n-1,k-1)
