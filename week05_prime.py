def is_prime(number:int) -> bool:
    """
    decimal determinant variable
    """
    is_prime = True

    if (number >= 2):
        i = 2
        for i in range(2, int(number**0.5)+1):
            # while( i * i <= number):
            if number % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True

n1 = int(input())
n2 = int(input())

if n1 > n2 :
    n1, n2 = n2, n1

for i in range(n1, n2+1):
    if is_prime(i):
        print(i, end=' ')
