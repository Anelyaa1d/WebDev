n = int(input())
a = [int(x) for x in input().split()]
b = 0
for i in range(1, n):
	if a[i] > a[i-1] :
		b = b + 1
print(b)
