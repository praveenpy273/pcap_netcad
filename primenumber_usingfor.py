def is_prime(num):
    if num == 1:
        return False
    for i in range(2,num+1):
        if i == num:
            return True
        div = num % i
        if div != 0:
            continue
        else:
            return False

x = is_prime(int(input('Enter any integer: ')))
print(x)
