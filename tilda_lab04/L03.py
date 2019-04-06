# -*- coding: iso-8859-1 -*-
# Copyright 2019, Axel Zedigh, All rights reserved.

class Node():

	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

class Bintree():

	def __init__(self, data = None, left = None, right = None):
		self.root = None

	def getRoot(self):
		return self.root.data

	def __contains__(self, value):
		"""
		Kollar om ett värde finns i trädet. "nyckel in trädobjekt"
		"""
		return self.finns(value, self.root)

	def put(self, data):
		"""
		Sätter in ny data i binärträdet.
		"""
		if self.root == None:
			self.root = Node(str(data))
		else:
			self._put(data, self.root)

	def _put(self, data, node):
		data = str(data)
		if data < node.data:
			if node.left is not None:
				self._put(data, node.left)
			else:
				node.left = Node(str(data))
		elif data > node.data:
			if node.right is not None:
				self._put(data, node.right)
			else:
				node.right = Node(str(data))

	def finns(self, data, node):
		if node is not None:	
			if str(data) > str(node.data): 
				if node.right:
					return self.finns(data, node.right)
				else:
					return False
			elif str(data) < str(node.data):
				if node.left:
					return self.finns(data, node.left)
				else:
					return False
			else:
				return True

	def write(self, order = "inorder"):
		"""
		Skriver ut trädet i inorder.
		"""
		if self.root is not None:
			if order == "inorder":
				self.inorder(self.root)
			elif order == "postorder":
				self.postorder(self.root)
			elif order == "preorder":
				self.preorder(self.root)
			else:
				raise NameError("Choose in-, pre- or postorder!")
			print("")

	def inorder(self,p = None):
		if p != None:
			self.inorder(p.left)
			print(p.data, sep=" ", end=" ")
			self.inorder(p.right)

	def preorder(self,p = None):
		if p != None:
			print(p.data, sep=" ", end=" ")
			self.preorder(p.left)
			self.preorder(p.right)

	def postorder(self,p = None):
		if p != None:
			self.postorder(p.left)
			self.postorder(p.right)
			print(p.data, sep=" ", end=" ")

def main():
	b = Bintree()
	b.put("pet")
	b.put("ubu")
	b.put(1)
	b.put("kan")
	b.put("aha")
	b.put("ret")
	b.write("preorder")
	#print(b.getRoot())
	if "ubu" in b: print("yes")
	else: print("no")
	#if b._finns("ubu", b.root) == None:
	#	print(True)


if __name__ == "__main__":
	main()