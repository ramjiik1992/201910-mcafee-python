
def find_primes():
    min=int(input('min?')) # min is also a python builtin function
    max=int(input('max?')) # it overwritten and unavailable to find_primes
    result=[]

    for number in range(min,max):
        for test in range(2,i):
            if number % test == 0 :
                break
        if test==number:
            print(number, end='\t')


find_primes()
# min the python function is still availble in global context
print('min value is ',min(2,9,8,1,11,3))  
# PROBLEM 1: Its a legally valid code
# PROBLEM 2: It just killed the print()
print='Hi'
find_primes()