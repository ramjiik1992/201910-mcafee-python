#business tier
def find_primes(min,max):
    result=[]
  
    for number in range(min,max):
        for test in range(2,number):
            if number % test == 0 :
                break
        else:
            result.append(number)
  
    return result


def prime_n(n, start=2):
    count=0
    number=start
    
    while count<n:
        for test in range(2,number):
            if number%test==0:
                break;
        else: # number is prime
            prime=number
            count+=1

        number+=1

    return prime
            




# presentation tier or app tier 
min=int(input('min?')) 
max=int(input('max?')) 

primes=find_primes(min,max)



print(primes)

print('prime#1', prime_n(1)) # should be 2

print('prime#25', prime_n(25)) # should be 97

print('prime#26', prime_n(26)) # should be 101

print('prime#1 after 100', prime_n(1,100)) # should be 101
