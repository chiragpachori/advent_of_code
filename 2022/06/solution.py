a = open('input').read()

for i in range(0, len(a)):
    if len(set(a[i:i+4])) == 4:
        print(set(a[i:i+4]))
        print(i+4)
# Change 4 to 14 for part 2

# One liner
print([i+4 for i in range(0, len(a)) if len(set(a[i:i+4])) == 4][0])
print([i+14 for i in range(0, len(a)) if len(set(a[i:i+14])) == 14][0])
