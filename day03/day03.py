
def getForest(filename):
	forest = []
	with open(filename,'r') as infile:
		for line in infile:
			forest.append(list(line.rstrip()))
	return forest

def treeEncounters(forest,start,slope):
	#x, y is start position
	x = start[0]
	y = start[1]
	tree_encounters = 0
	xmax = len(forest[0])
	ymax = len(forest)
	while y < ymax:
		if(forest[y][x%xmax] == '#'):
			tree_encounters += 1
		x += slope[0]
		y += slope[1]
	return tree_encounters

def testForest():
	forest = []
	forest.append(list("..##......."))
	forest.append(list("#...#...#.."))
	forest.append(list(".#....#..#."))
	forest.append(list("..#.#...#.#"))
	forest.append(list(".#...##..#."))
	forest.append(list("..#.##....."))
	forest.append(list(".#.#.#....#"))
	forest.append(list(".#........#"))
	forest.append(list("#.##...#..."))
	forest.append(list("#...##....#"))
	forest.append(list(".#..#...#.#"))
	return forest
	
if __name__ == "__main__":
	forest = getForest("input.txt") # a 2-d array of the trees
	start = [0,0] # x,y starting point
	slope = [3,1] # right,down
	print(treeEncounters(forest,start,slope)) # part01 answer
	
	product = 1
	slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
	for slope in slopes:
		product *= treeEncounters(forest,start,slope)
	print(product) # part02 answer

	
