import random
import math
from harm import*

PRIORITY_SIZE = 0x7fffffff

class Treap_node(object):
	__slots__ = ('priority', 'key', 'left', 'right', 'parent')

	def __init__(self, wieght = 1, key = None, left = None, right = None, parent = None):
		rList = [int(random.random() * PRIORITY_SIZE) for x in range(wieght)]
		self.priority = max(rList)
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent

	def rotate_right(self):
		y = self
		x = y.left
		B = x.right
		y.left = B
		x.right = y
		if B is not None:
			B.parent = y
		x.parent = y.parent
		y.parent = x
		if x.parent is not None:
			parent = x.parent
			if parent.left is y:
				parent.left = x
			else:
				parent.right = x
		return x

	def rotate_left(self):
		x = self
		y = x.right
		B = y.left
		x.right = B
		y.left = x
		if B is not None:
			B.parent = x
		y.parent = x.parent
		x.parent = y
		if y.parent is not None:
			parent = y.parent
			if parent.left is x:
				parent.left = y
			else:
				parent.right = y
		return y

	def __str__(self):
		p = "+" if self.parent is not None else "None"
		l = "+" if self.left is not None else "None"
		r = "+" if self.right is not None else "None"
		return "Parent : "+p+"	"+"Left : "+l+"	"+"Right : "+r+"	"+"Key : "+str(self.key)+"	"+"Priority : "+str(self.priority)

class Treap(object):

	def __init__(self, handles = False):
		self.root = None
		self.size = 0
		self.handles = handles

	def find(self, key):
		current = self.root
		count = 0
		while True:
			count += 1
			if current is None:
				return KeyError
			elif key > current.key:
				current = current.right
			elif key < current.key:
				current = current.left
			else:
				return (count,current)

	def insert(self, node):
		if self.root == None:
			self.root = node
			self.size += 1
			count = 1
		else:
			current = self.root
			count = 0
			while True:
				if not self.handles:
					count += 1
				if node.key > current.key:
					if current.right is not None:
						current = current.right
					else:
						current.right = node
						node.parent = current
						self.size += 1
						break
				elif node.key < current.key:
					if current.left is not None:
						current = current.left
					else:
						current.left = node
						node.parent = current
						self.size += 1
						break
				else:
					raise KeyError
			while current is not None:
				if node.priority > current.priority:
					count += 1
					if node.key > current.key:
						current = current.rotate_left().parent
					else :
						current = current.rotate_right().parent
				else:
					break

			if current is None:
				self.root = node

		return count

	def delete(self, key):
		count = 0
		if self.root is None:
			pass
		else:
			count,node = self.find(key)
			if self.handles:
				count = 0
			isRoot = False
			if node is self.root:
				isRoot = True
			while node.left is not None and node.right is not None:
				if node.left.priority > node.right.priority:
					if isRoot:
						self.root = node.rotate_right()
						isRoot = False
					else:
						node.rotate_right()
					count += 1
				else:
					if isRoot:
						self.root = node.rotate_left()
						isRoot = False
					else:
						node.rotate_left()
					count += 1

			if node.left is None and node.right is None:
				if node.parent == None:
					self.root = None
				elif node.parent.left is node:
					node.parent.left = None
				else:
					node.parent.right = None
			elif node.left is None:
				if node.parent == None:
					self.root = node.right
				elif node.parent.left is node:
					node.parent.left = node.right
				else:
					node.parent.right = node.right
				node.right.parent = node.parent
			elif node.right is None:
				if node.parent == None:
					self.root = node.left
				elif node.parent.left is node:
					node.parent.left = node.left
				else:
					node.parent.right = node.left
				node.left.parent = node.parent
			return count+1

def main():
	buildHarmonique(2000)
	keys = list(range(1,2000))
	add = [0]*len(keys)
	find = [0]*len(keys)
	find1 = [0]*len(keys)
	find2 = [0]*len(keys)
	find3 = [0]*len(keys)
	find4 = [0]*len(keys)
	delete = [0]*len(keys)
	addT = [0]*len(keys)
	deleteT = [0]*len(keys)
	n = 1000
	random.shuffle(keys)
	for i in range(n):
		treapT = Treap(True)
		treap = Treap()
		for i,key in enumerate(keys):
			addT[i]+=treapT.insert(Treap_node(key = key))
			add[i]+=treap.insert(Treap_node(key = key))
			s = sorted(keys[:i+1])
			find1[i]+=treap.find(s[i//10])[0]
			find2[i]+=treap.find(s[i//4])[0]
			find3[i]+=treap.find(s[i//2])[0]
			find[i]+=treap.find(keys[random.randint(0,i)])[0]

		for i,key in enumerate(keys):
			delete[len(keys)-1-i]+=treap.delete(key)
			deleteT[len(keys)-1-i]+=treapT.delete(key)

	for i in range(len(keys)):

		const1 = H[i//10+1]+H[i*9//10+1]-1
		const2 = H[i//4+1]+H[i*3//4+1]-1
		const3 = H[i//2+1]+H[i//2+1]-1
		res = [str(i),str(addT[i]/n),str(deleteT[i]/n),str(add[i]/n),str(delete[i]),str(find[i]/n),str(find1[i]/n),str(const1),str(find2[i]/n),str(const2),str(find3[i]/n),str(const3)]
		print("\t".join(res))

if __name__ == '__main__':
	main()