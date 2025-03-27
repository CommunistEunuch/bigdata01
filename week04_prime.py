def is_prime(number):
    """
    decimal determinant variable
    """
    is_prime = True

    if (number >= 2):
        i = 2
        while (i * i <= number):
            # for i in range(2, number):
            if number % i == 0:
                return False
            #print(i, end=" ")
            i = i + 1
    else:
        return False
    return True


number = int(input())
if is_prime(number):
    print(f"{number}는 소수입니다")
else : print(f"{number}는 소수가 아닙니다")