import random

user_input = random.randint(0,20)
print(user_input)

fact = 1

if user_input == 0:
	print(1)
	exit
else:
	for i in range(1,user_input+1):
		fact = fact * i
	print(fact)


