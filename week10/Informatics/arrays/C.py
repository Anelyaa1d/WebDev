n = int(input())
a = [int(x) for x in input().split()]
r = 0
for i in range(0, len(a)):
	if a[i] > 0 :
		r = r + 1
print(r)
