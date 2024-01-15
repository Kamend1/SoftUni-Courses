counter = int(input())
usernames = set()

for _ in range(counter):
    username = input()
    usernames.add(username)

print(*usernames, sep='\n')
