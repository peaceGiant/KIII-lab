# Initial distribution should look like [1, 0, 0]
def init_distribution():
	return [0, 0, 1]

# 2 should multiply all elements, not repeat the list 2 times
def scale_distribution(h: list[int]):
	return 2 * list(h)
