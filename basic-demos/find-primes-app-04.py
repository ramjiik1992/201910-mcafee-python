#business tier
def find_primes(min,max):
    result=[]
    #min=int(input('min?')) # presentation tier logic in business tier
    #max=int(input('max?')) # violates Single responsibility principle (SRP)

    for number in range(min,max):
        #prime=True
        for test in range(2,number):
            if number % test == 0 :
                #prime=False
                break
        else:
            result.append(number)
            #print(number, end='\t') viloates SRP
    return result


# presentation tier or app tier 
min=int(input('min?')) # min is also a python builtin function
max=int(input('max?')) # it overwritten and unavailable to find_primes

primes=find_primes(min,max)
print(primes)
