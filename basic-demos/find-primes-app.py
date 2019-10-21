import primeutils as pu

def main():
    min=int(input('min?')) 
    max=int(input('max?')) 

    primes=pu.find_primes(min,max)

    print(primes)

    x=pu.PrimeUtils()
    primes=x.find_primes(2,10)
    print(primes)
    



if __name__!='__main__':
    raise Exception('Not an importable module!')

main()



