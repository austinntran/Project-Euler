import math


def main():
    num = 600851475143
    for i in range(int(math.sqrt(num)), 1, -1):
        if i % 2 == 0 or num % i != 0 or checkPrime(i) == 0:
            continue
        print(i)
        break




def checkPrime(p):
    for i in range(2, int(math.sqrt(p))):
        if p % i == 0:
            return 0
    return 1

if __name__ == "__main__":
    main()