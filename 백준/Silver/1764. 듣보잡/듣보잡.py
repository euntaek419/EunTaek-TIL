n, m = map(int, input().split())

people = {}
result = []

for i in range(n+m):
    name = input()
    if(name in people):
        result.append(name)
    else:
        people[name] = 1

result.sort()

print(len(result))

for i in result:
    print(i)