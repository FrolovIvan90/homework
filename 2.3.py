n = int(input())
i = 1
an = ''
while i < n:
    i = i * 2
    if i == n:
        an = 'YES'
    else:
        an = 'NO'
print(an)
