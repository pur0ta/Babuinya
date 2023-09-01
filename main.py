def sum_lists(a, b):
	c = a.copy()
	for i in range(len(b)):
		c[i] = c[i] + b[i]
	return c

