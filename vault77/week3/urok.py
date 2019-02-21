lst = [5, 6, 3, 2, 1, 10]

def dell(idx, lst):
	return [lst[i] for i in range(len(lst)) if i != idx]

print(dell(4, lst))