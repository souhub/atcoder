numbers = []

while True:
    number = input()
    if number == '0':
        break
    numbers.append(number)

for number in numbers:
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    print(sum)
