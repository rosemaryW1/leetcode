a = '745abcd'

sum = 0

for x in a:
    if x.isdigit():
        sum = sum + int(x)
print(sum)