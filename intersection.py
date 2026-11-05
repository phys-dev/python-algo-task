from hash_table import HashSet


first = HashSet(int(value) for value in input().split())
second = HashSet(int(value) for value in input().split())
print(*sorted(value for value in first if value in second))
