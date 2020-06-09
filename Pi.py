import random
import time
from math import pow

def estimate_pi(n):

	num_circle = 0
	num_total  = 0

	for i in range(n):
		x = random.uniform(0,1)
		y = random.uniform(0,1)
		dist = pow(x,2) + pow(y,2)

		if dist <=1:
			num_circle += 1
		num_total += 1

	return 4 * (num_circle/num_total)


sample = int(input ("Enter sample size: "))


#print (time.asctime( time.localtime(time.time()) ))
start = time.time()

print(estimate_pi(sample))

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Total time : {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
