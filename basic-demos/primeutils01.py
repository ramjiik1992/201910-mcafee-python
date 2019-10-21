#business tier

#def IsPrime(number):  # python method names follow snake case not Pascal case
def is_prime(number):
    if number<2:
        return False
    
    for test in range(2,number):
        if number % test == 0 :
            return False
    return True

def find_primes(min,max):
    result=[]
  
    for number in range(min,max):
        if is_prime(number):
            result.append(number)
  
    return result


def prime_n(n, start=2):
    count=0
    number=start
    
    while count<n:
        if is_prime(number):
            prime=number
            count+=1

        number+=1

    return prime
            

# presentation tier or app tier 
if __name__=='__main__':
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
    