import time

print("2 seconds break")

time.sleep(2000)


def fun(scores):
	assert len(scores) != 0, 'List should not be empty'
	return sum(scores)/len(scores)


scores = list(map(int,input().split())
print(fun(scores))


