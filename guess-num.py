import random

r = random.randint(1, 100)
print(f"random number = {r}")
count = 0

while True:
	count += 1
	num = input('guess number:')
	num = int(num)
	if num == r:
		print('猜中了 !')
		print(f"猜了 {count} 次")
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print(f"猜了 {count} 次")