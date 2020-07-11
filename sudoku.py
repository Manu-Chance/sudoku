import numpy as np

'''
puzzle = [      [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
         ]
'''

puzzle = [      [3,0,0,8,0,1,0,0,2],
                [2,0,1,0,3,0,6,0,4],
                [0,0,0,2,0,4,0,0,0],
                [8,0,9,0,0,0,1,0,6],
                [0,6,0,0,0,0,0,5,0],
                [7,0,2,0,0,0,4,0,9],
                [0,0,0,5,0,9,0,0,0],
                [9,0,4,0,8,0,7,0,5],
                [6,0,0,1,0,7,0,0,3],
         ]



def sol_checker(x,y,n):
	for i in range(0, 9):
		if puzzle[y][i] == n or puzzle[i][x] == n:
			return False

	pos_x = (x // 3) * 3
	pos_y = (y // 3) * 3

	for i in range(0, 3):
		for j in range(0, 3):
			if puzzle[pos_y + i][pos_x + j] == n:
				return False
	return True


def solve():
	for y in range(9):
		for x in range(9):
			if puzzle[y][x] == 0:
				for n in range(1, 10):
					if sol_checker(x,y,n):
						puzzle[y][x] = n
						solve()
						puzzle[y][x] = 0
				return

	print(np.matrix(puzzle))
	input("More?")

solve()

#print(sol_checker(4,4,5))


