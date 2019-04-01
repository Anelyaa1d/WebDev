def pows(a, n): 
#	p = 1
#	for i in range(0, n):
#		p = p * a
	return pow(a, n)
if __name__ == '__main__':
	a = raw_input().split(' ')
	n = raw_input().split(' ')
	print(pows(a, n))
