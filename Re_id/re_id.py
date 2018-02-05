def generate_prime(max_range):
    seed = list(range(2, max_range))
    while not len(seed) == 0:
        top = seed.pop(0)
        yield top
        seed = [i for i in seed if not i % top == 0]

def answer(n):
    prime = list(generate_prime(21000))

    primes=  ''.join(map(str, prime))
    print primes

    for idx, val in enumerate(primes):
        print idx,val
        if idx == n:
            final=primes[idx:idx+5]
            return ''.join(map(str, final))


    return -1

n = 10000
print(answer(n))
