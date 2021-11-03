def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i <= num:
        if i == num:
            return True
        div = num % i

        if div != 0:
            i = i + 1
        else:
            return False

x = is_prime(int(input('Enter any integer : ')))
print(x)
