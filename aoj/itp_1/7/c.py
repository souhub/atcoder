r, c = map(int, input().split())

table = []

for i in range(r):
    line = list(map(int, input().split()))
    table.append(line)

# Caluculate the total sum of the elements.
sum_all = 0
for k in range(r):
    for l in range(c):
        sum_all += table[k][l]

# Calculate the sum of the each row.
for k in range(r):
    sum_r = 0
    for l in range(c):
        sum_r += table[k][l]
    table[k].append(sum_r)

# Calculate the sum of the each column.
new_col = []

for l in range(c):
    sum_c = 0
    for k in range(r):
        sum_c += table[k][l]
    new_col.append(sum_c)
    if l == c-1:
        new_col.append(sum_all)

table.append(new_col)

# Output the answer.
for r in table:
    print(*r)
