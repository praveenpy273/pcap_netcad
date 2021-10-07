# take any non-negative and non-zero integer number and name it c0;if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0,it will always go to 1.
# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. 
# We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

c0 = int(input('Enter a non- negative, non-zero integer: '))
step = 0

while True:
    if c0 % 2 == 0:
        c0 //= 2
        if c0 != 1:
            step += 1
            print(' New value is ', c0, ':', 'step', step)
            continue
        elif c0 == 1:
            step += 1
            print(' New value is ', c0, ':', 'step', step)
            break
    elif c0 % 2 == 1:
        c0 = c0 * 3 + 1
        if c0 != 1:
            step += 1
            print(' New value is ', c0, ':', 'step', step)
            continue
        elif c0 == 1:
            step += 1
            print(' New value is ', c0, ':', 'step:', step)
            break
            
print('Total Steps: ', step)
