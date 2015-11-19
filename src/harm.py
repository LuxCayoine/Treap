import math
H = {}

def buildHarmonique(k):
	H[0] = 1
	H[1] = 1
	for i in range(2,k+1):
		H[i] = H[i-1]+1/i

def find(n):
	res = 0
	for j in range(1,n+1):
		# res+= H[j]+H[n+1-j]-1
		print(str(j)+"\t"+str(H[j]+H[n+1-j]-1))
	return res/n

if __name__ == '__main__':
	buildHarmonique(10000)
	# for i in range(1,10000):
	# 	print(str(i)+"\t"+str(find(i)))

	# for i in range(1,10000):
	# 	print(str(2*math.log(i)+1)+"\t"+str(2*math.log(i)-2)+"\t"+str(2*math.log(i)))

	find(10000)