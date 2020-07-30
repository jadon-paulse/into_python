
start_p = int(input("Enter the start point N: "))
end_p = int(input("Enter the end point M: "))

def isPrime(n):
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

for n in range(start_p, end_p):
    if str(n) == str(n)[::-1] and isPrime(n):
        print(n)