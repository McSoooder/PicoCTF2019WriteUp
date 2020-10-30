from math import gcd

def GetInput(term):
    inputValue = input("Enter {0}:".format(term))
    inputValue.strip()
    try:
        return int(inputValue)
    except:
        print("Value was not a number.")
        return GetInput(term)

def PrintMenu():
    print("1. Calculate n.")
    print("2. Calculate p/q.")
    print("3. Calculate totient(n)")
    print("4. Print this menu.")
    print("5. Encrypt.")
    print("6. Decrypt")
    print("7. Exit")

def CalculateN(p,q):
    return p*q

def CalculatePorQ(qorp, n):
    return int(n/qorp)

def CalculateTotient(x):
    primes = 0
    for y in range(0,x):
        if gcd(y,x) == 1:
            primes = primes+1

    return primes

def EncryptPlaintext(e,n):
    plaintext = GetInput("plaintext")
    ciphertext = pow(plaintext,e,n)
    print("Ciphertext:\n{0}".format(ciphertext))

def CalculateInverse(e,n):
    return pow(e,-1,n)

def DecryptCiphertext(e,n):
    ciphertext = GetInput("ciphertext")
    d = CalculateInverse(e,n)
    if d != 0:
        plaintext = pow(ciphertext,d,n)
        print("d:\n{0}\nPlaintext:\n{1}".format(d,plaintext))
    else:
        print("Error: Inverse (d) could not be found.")

def PrintPQN(p,q,n):
    print("p:\n{0}\nq:\n{1}\nn:\n{2}".format(p,q,n))

if __name__ == "__main__":
    PrintMenu()
    choice = GetInput("choice")
    while choice != 4:
         if choice == 1:
             p = GetInput("p")
             q = GetInput("q")
             n = CalculateN(p,q)
             PrintPQN(p,q,n)
         if choice == 2:
             porq = GetInput("known p/q")
             n = GetInput("n")
             qorp = CalculatePorQ(porq, n)
             PrintPQN(porq,qorp, n)

         if choice == 3:
             p = GetInput("p")
             q = GetInput("q")
             n = CalculateN(p,q)
             totient = CalculateTotient(n)
             print("Totient n:\n{0}".format(primes))

         if choice == 4:
             q = GetInput("q")
             p = GetInput("p")
             e = GetInput("e")
             n = q*p
             print("n\n{0}\n".format(n))
             CalculateInverse(n,e)

         if choice == 5:
             PrintMenu()

         if choice == 6:
             e = GetInput("e")
             n = GetInput("n")
             EncryptPlaintext(e,n)
         if choice == 7:
             e = GetInput("e")
             n = GetInput("n")
             DecryptCiphertext(e,n)

         choice = GetInput("choice")
