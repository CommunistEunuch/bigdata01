def is_prime(number):
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


number = int(input())
if is_prime(number):
    print(f"{number}는 소수입니다")
else : print(f"{number}는 소수가 아닙니다")