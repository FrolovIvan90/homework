N = int(input())

sum = 0

while N > 0:
     d = N%10
     N = N// 10
     sum += d
     print(sum)
