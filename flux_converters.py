def answer(h, q):
	t = (2 ** h)-1
	for i in range(len(q)):
		if q[i] == t: q[i] = -1
		else: q[i] = parent(q[i], t, h)
	return q

def parent(e, n, h):
	if h == 1: return 
	left = n - (2 ** (h-1))
	right = n - 1
	if left == e or right == e:
		return n
	return parent(e, left, h-1) or parent(e, right, h-1)