import math

n = int(input())

input_numbers = []

for _ in range(n):
    input_numbers.append(int(input()))

# Reference https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
max_number = max(input_numbers)

limit = math.sqrt(max_number)

numbers = [i for i in range(2, max_number+1)]

prime = []

while True:
    p = numbers[0]
    if limit <= p:
        numbers = prime+numbers
        break
    prime.append(p)
    numbers = [e for e in numbers if e % p != 0]

cnt = 0

for i_n in input_numbers:
    for n in numbers:
        if i_n == n:
            cnt += 1

print(cnt)
