def sum_lists(a, b):
	c = a.copy()
	for i in range(len(b)):
		c[i] = c[i] + b[i]
	return c

def multiply_lists(a, b):
	if len(a) > len(b):
		c = a.copy()
		for i in range(len(b)):
			c[i] = c[i] * b[i]
	else:
		c = b.copy()
		for i in range(len(a)):
			c[i] = c[i] * a[i]
	return c

