
def reverse(f, N):
    F = [f(0)]

    for n in range(1, N):
        F.append( (-1) / f(0) * sum([
                f(k) * F[n-k] for k in range(1, n+1)
            ])
        )
    
    return F


# print(reverse(lambda n: 1, 10))
# print(reverse(lambda n: 2**n, 10))
# print(reverse(rec := lambda n: n * rec(n-1) if n > 0 else 1 , 10))
# print(reverse(rec := lambda n: 1/n * rec(n-1) if n > 0 else 1 , 10))

# print(reverse(fib := lambda n: fib(n-1) + fib(n-2) if n > 1 else 1 , 10))
print(reverse(lambda n: 1/(1-n)**n if n>1 else 1, 10))
print(reverse(lambda n: 1 , 10))