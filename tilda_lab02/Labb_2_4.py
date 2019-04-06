# -*- coding: iso-8859-1 -*-
from arrayQFile import ArrayQ 


if __name__ == "__main__":
	q = ArrayQ()
	q.enqueue(1)
	q.enqueue(2)
	x = q.dequeue()
	y = q.dequeue()
	if (x == 1 and y == 2):
		print("Fungerar")
	else:
		print("Något är fel. 1 och 2 förväntades men vi fick", x, y)
	s = ArrayQ()
	q.trolleri()