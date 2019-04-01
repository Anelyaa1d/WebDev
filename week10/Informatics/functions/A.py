# def Mini(a, b):
# 	if(a < b):
# 		return a
# 	else:
# 		return b;
# def Minim(a, b, c, d):
# 	mini = int(a)
# 	mini = Mini(mini, b)
# 	mini = Mini(mini, c)
# 	mini = Mini(mini, d)
# 	return mini
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(Minim(a, b, c, d))

def mini(s):
	return min(s)


if __name__ == '__main__':
	s = input().split(' ')
	print(mini(s))