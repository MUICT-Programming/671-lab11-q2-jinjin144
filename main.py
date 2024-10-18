def summation(lst1, lst2):
    updated_list = [a + b for a, b in zip(lst1, lst2)]
    return updated_list

def find_min_max(updated_list):
    return (min(updated_list), max(updated_list))

n = int(input())
lst1 = []
lst2 = []

print()
for i in range(n):
    lst1.append(int(input()))

print()
for y in range(n):
    lst2.append(int(input()))

updated_list = summation(lst1, lst2)
min_max = find_min_max(updated_list)

print(updated_list)
print(min_max)
