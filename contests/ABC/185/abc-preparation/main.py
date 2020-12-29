def linear_minimum_number_search(a_list: list[int]) -> min:
    min = a_list[0]
    for l in range(1, len(a_list)):
        if min > a_list[l]:
            min = a_list[l]
    return min


# a_list = list(map(int, input().split()))
# min = linear_minimum_number_search(a_list)
# print(min)

a, b, c, d = map(int, input().split())
print(min(a, b, c, d))
