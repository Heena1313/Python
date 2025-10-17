a=5
for i in range(1,11):
    print(f"{a} * {i} = {a*i}")

print(" ")
for i in range(6):
  print("*"*i)

print(" ")
for i in range(6,0,-1):
    print("*"*i)


n = 5
print(" ")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

print(" ")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))

print(" ")

for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))
