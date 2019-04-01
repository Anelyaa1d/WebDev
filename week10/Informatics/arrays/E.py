
n = int(input())
a = [int(x) for x in input().split()]
ok = False
for i in range(0, n-1):
	if a[i] * a[i+1] >= 0 :
		ok = True
		break
if ok :
	print("YES")
else :
	print("NO")
