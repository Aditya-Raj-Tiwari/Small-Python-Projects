def primeNumberCalc(givenNumber):
    primes = []
    primeFact = []
    for possiblePrime in range(2, givenNumber + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)

    for numbs in primes:
        if givenNumber % numbs == 0:
            primeFact.append(numbs)

    return (primeFact)


try:
    print(primeNumberCalc(int(input('Please enter a number you want to find factors of: '))))
except ValueError:
    print('Only Numbers are expected.')
