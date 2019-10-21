from primeutils import is_prime, find_primes

def test():
    range={2:True, 4:False, 0:True, -2:False, 13:True}
    error=0
    for (value,expectedResult) in range.items():
        actualResult=is_prime(value)
        if actualResult!=expectedResult:
            print(f'Failed for {value}. expected was {expectedResult} found {actualResult}')
            error+=1

    if error:
        print(f'{error}/{len(range)} test failed')
    else:
        print('all test passed')
    primes=find_primes(0,100)
    print(primes)


test()