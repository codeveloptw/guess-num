import random

r = random.randint(1, 100)
print(f"random number = {r}")

while True:
	num = input('guess number:')
	num = int(num)
	if num == r:
		print('righ !')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')