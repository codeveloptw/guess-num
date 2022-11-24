import random

top = 100
down = 0

r = random.randint(down, top)
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
		top = num
		print(f"比答案大, Number between {down} and {top}")
	elif num < r:
		print('比答案小')
		down = num
		print(f"比答案大, Number between {down} and {top}")		
	print(f"猜了 {count} 次")