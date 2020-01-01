matrix = [
    [50, 45, 37, 32, 30],
    [35, 50, 40, 20, 25],
    [30, 30, 25, 17, 28],
    [27, 24, 22, 15, 10]
]
vertical = len(matrix)
horizontal = len(matrix[0])

memory = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

def find_paths(mat, st, ed):
    if st == ed:
        print(st, ed)
        return 1
    
    x, y = st

    if memory[y][x] == -1:
        memory[y][x] = 0
        
        # move up
        if y > 0 and matrix[y][x] > matrix[y-1][x]:
            memory[y][x] += find_paths(mat, [x, y-1], ed)
        # move down
        if y < vertical-1 and matrix[y][x] > matrix[y+1][x]:
            memory[y][x] += find_paths(mat, [x, y+1], ed)
        # move left
        if x > 0 and matrix[y][x] > matrix[y][x-1]:
            memory[y][x] += find_paths(mat, [x-1, y], ed)
        # move right
        if x < horizontal-1 and matrix[y][x] > matrix[y][x+1]:
            memory[y][x] += find_paths(mat, [x+1, y], ed)
    return memory[y][x]
    


def main():
    start = [0, 0] # row, column
    end = [len(matrix[0])-1, len(matrix)-1] # row, column

    print(find_paths(matrix, start, end))
    [print(m) for m in memory]


if __name__ == "__main__":
    main()