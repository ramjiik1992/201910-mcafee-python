def find_primes():
    min=int(input('min?')) # min is also a python builtin function
    max=int(input('max?')) # it overwritten and unavailable to find_primes
    result=[]

    for number in range(min,max):
        prime=True
        for test in range(2,number):
            if number % test == 0 :
                prime=False
                break
        if prime:
            print(number, end='\t')

find_primes()
